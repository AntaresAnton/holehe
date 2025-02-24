import trio
import httpx
import logging
from colorama import init, Fore, Style
from datetime import datetime
from holehe.core import get_functions
from holehe import modules
import importlib
import pkgutil

def import_submodules(package, recursive=True):
    print(Fore.YELLOW + f"Scanning package: {package}" + Style.RESET_ALL)
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        print(Fore.CYAN + f"Found module: {name}" + Style.RESET_ALL)
        full_name = package.__name__ + '.' + name
        try:
            results[full_name] = importlib.import_module(full_name)
            print(Fore.GREEN + f"Successfully imported: {full_name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error importing {full_name}: {str(e)}" + Style.RESET_ALL)
        if recursive and is_pkg:
            print(Fore.YELLOW + f"Recursively scanning: {full_name}" + Style.RESET_ALL)
            results.update(import_submodules(full_name))
    return results

async def main():
    print(Fore.CYAN + "=== HOLEHE Module Health Check ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "Starting module discovery..." + Style.RESET_ALL)
    
    try:
        print(Fore.CYAN + "Importing holehe.modules..." + Style.RESET_ALL)
        all_modules = import_submodules('holehe.modules')
        print(Fore.GREEN + f"Found {len(all_modules)} module files" + Style.RESET_ALL)
        
        modules_list = []
        for name, mod in all_modules.items():
            print(Fore.YELLOW + f"Checking module: {name}" + Style.RESET_ALL)
            if hasattr(mod, '__call__'):
                modules_list.append(mod)
                print(Fore.GREEN + f"Added callable module: {name}" + Style.RESET_ALL)
        
        print(Fore.CYAN + f"\nTotal callable modules found: {len(modules_list)}" + Style.RESET_ALL)
        
        # Rest of your existing code...
        
    except Exception as e:
        print(Fore.RED + f"Error during module discovery: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    init()
    trio.run(main)
