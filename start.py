from imports import *

# Configure logging
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'holehe_check_{timestamp}.log'),
        logging.StreamHandler()
    ]
)

init()

async def main():
    print(Fore.CYAN + "=== HOLEHE Email Checker ===" + Style.RESET_ALL)
    email = input(Fore.GREEN + "Enter email to check: " + Style.RESET_ALL)
    
    logging.info(f"Starting check for email: {email}")
    
    out = []
    client = httpx.AsyncClient(timeout=30.0)
    
    check_functions = [
        discord, github, instagram, twitter, snapchat,  # social media
        adobe, wordpress, voxmedia,  # cms
        hubspot, zoho, insightly, nimble, pipedrive,  # crm
        google, yahoo,  # mails
    ]
    
    logging.info(f"Loaded {len(check_functions)} modules to check")
    print(Fore.YELLOW + f"\nChecking {len(check_functions)} websites..." + Style.RESET_ALL)
    
    for check in check_functions:
        try:
            print(Fore.CYAN + f"Checking {check.__name__}..." + Style.RESET_ALL, flush=True)
            logging.info(f"Starting check for {check.__name__}")
            await check(email, client, out)
            logging.info(f"Completed check for {check.__name__}")
            await trio.sleep(0.5)
        except Exception as e:
            logging.error(f"Error in {check.__name__}: {str(e)}")
            continue
    
    print(Fore.YELLOW + "\nResults:" + Style.RESET_ALL)
    for result in out:
        if result and result.get("exists"):
            msg = f"Account found on {result['name']}"
            logging.info(msg)
            print(Fore.GREEN + f"✔ {msg}" + Style.RESET_ALL)
    
    report_file = generate_html_report(email, out)
    print(Fore.CYAN + f"\nHTML Report generated: {report_file}" + Style.RESET_ALL)
    
    logging.info("Check completed")
    await client.aclose()

if __name__ == "__main__":
    trio.run(main)
