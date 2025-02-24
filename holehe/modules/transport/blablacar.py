import trio
import httpx
import logging
import datetime
import json
from holehe.core import get_functions
from holehe import modules
from colorama import init, Fore, Style

init()

# Set up logging
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'holehe_log_{timestamp}.log'),
        logging.StreamHandler()
    ]
)

async def main():
    print(Fore.CYAN + "=== HOLEHE Email Checker ===" + Style.RESET_ALL)
    email = input(Fore.GREEN + "Enter email to check: " + Style.RESET_ALL)
    
    # Create results files
    json_file = f"results_{email}_{timestamp}.json"
    txt_file = f"results_{email}_{timestamp}.txt"
    
    logging.info(f"Starting check for email: {email}")
    print(Fore.YELLOW + "\nVerificando..." + Style.RESET_ALL)
    
    out = []
    client = httpx.AsyncClient(timeout=30.0)
    websites = get_functions(modules.__dict__)
    
    for website in websites:
        try:
            await website(email, client, out)
            await trio.sleep(0.5)
            logging.info(f"Checked {website.__name__}")
            print(Fore.YELLOW + f"Checking {website.__name__}..." + Style.RESET_ALL)
        except Exception as e:
            logging.error(f"Error checking {website.__name__}: {str(e)}")
            continue
    
    # Save results to JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=4)
        logging.info(f"Results saved to JSON: {json_file}")
    
    # Save results to TXT
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(f"Results for {email}\n")
        f.write("=" * 50 + "\n")
        for result in out:
            if result.get("exists"):
                status = "✔ Found"
                f.write(f"{status} - {result['name']}\n")
                logging.info(f"Account found on {result['name']}")
                print(Fore.GREEN + f"✔ Found account on: {result['name']}" + Style.RESET_ALL)
    
    logging.info("Check completed")
    print(Fore.CYAN + f"\nResults saved to:\n{json_file}\n{txt_file}" + Style.RESET_ALL)
    
    await client.aclose()

if __name__ == "__main__":
    trio.run(main)
