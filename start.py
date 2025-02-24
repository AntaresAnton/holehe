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
    bitmoji, crevado, discord, facebook, fanpop, imgur, instagram, myspace, odnoklassniki,
    parler, patreon, pinterest, plurk, snapchat, strava, taringa, tellonym, tumblr, twitter,
    vsco, wattpad, xing,  # social media
    atlassian, gravatar, voxmedia, wordpress,  # cms
    amocrm, axonaut, hubspot, insightly, nimble, nocrm, nutshell, pipedrive, teamleader, zoho,  # crm
    google, laposte, mail_ru, protonmail, yahoo,  # mails
    babeshows, badeggsonline, biosmods, biotechnologyforums, blackworldforum, blitzortung,
    bluegrassrivals, cambridgemt, chinaphonearena, clashfarmer, codeigniter, cpaelites,
    cpahero, cracked_to, demonforums, freiberg, koditv, mybb, nattyornot, ndemiccreations,
    nextpvr, onlinesequencer, thecardboard, therianguide, thevapingforum,  # forums
    ello, flickr, komoot, rambler, sporcle,  # media
    blip, lastfm, smule, soundcloud, spotify, tunefind,  # music
    pornhub, redtube, xnxx, xvideos,  # porn
    aboutme,  # company
    buymeacoffee,  # crowdfunding
    coroflot, freelancer, seoclerks,  # jobs
    diigo, duolingo, quora,  # learning
    caringbridge, sevencups,  # medical
    rocketreach,  # osint
    venmo,  # payment
    anydo, evernote,  # productivity
    eventbrite, nike, samsung,  # products
    codecademy, codepen, devrant, github, replit, teamtreehouse,  # programming
    vrbo,  # real estate
    amazon, armurerieauxerre, deliveroo, dominosfr, ebay, envato, garmin, naturabuy, vivino,  # shopping
    adobe, archive, docker, firefox, issuu, lastpass, office365,  # software
    bodybuilding,  # sport
    # blablacar  # transport
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
