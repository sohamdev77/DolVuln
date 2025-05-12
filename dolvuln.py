import requests
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init()

# Print the DolVuln Logo
print(Fore.GREEN + Style.BRIGHT + r"""

 ______   _______  _                          _        _       
(  __  \ (  ___  )( \      |\     /||\     /|( \      ( (    /|
| (  \  )| (   ) || (      | )   ( || )   ( || (      |  \  ( |
| |   ) || |   | || |      | |   | || |   | || |      |   \ | |
| |   | || |   | || |      ( (   ) )| |   | || |      | (\ \) |
| |   ) || |   | || |       \ \_/ / | |   | || |      | | \   |
| (__/  )| (___) || (____/\  \   /  | (___) || (____/\| )  \  |
(______/ (_______)(_______/   \_/   (_______)(_______/|/    )_)
                                                               
                                                                         
                  DolVuln v1.0 by Soham      
""" + Style.RESET_ALL)

# Basic vulnerability scan for open ports
def scan_ports(target):
    print(Fore.YELLOW + "\nScanning ports on " + target + "..." + Style.RESET_ALL)
    ports = [80, 443, 8080, 3000, 5000]
    for port in ports:
        url = f"http://{target}:{port}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(Fore.GREEN + f"Port {port} is open on {target}" + Style.RESET_ALL)
        except requests.exceptions.RequestException:
            print(Fore.RED + f"Port {port} is closed or unreachable." + Style.RESET_ALL)

# Basic vulnerability scan for outdated software based on HTTP headers
def scan_headers(target):
    print(Fore.YELLOW + "\nScanning HTTP headers for potential vulnerabilities..." + Style.RESET_ALL)
    try:
        response = requests.get(f"http://{target}", timeout=3)
        headers = response.headers
        if 'Server' in headers:
            server_info = headers['Server']
            print(Fore.RED + f"Server info leak: {server_info}" + Style.RESET_ALL)
    except requests.exceptions.RequestException:
        print(Fore.RED + "Could not reach the target for header scan." + Style.RESET_ALL)

def main():
    target = input(Fore.CYAN + "Enter target URL (e.g., example.com): " + Style.RESET_ALL)
    scan_ports(target)
    scan_headers(target)

if __name__ == "__main__":
    main()
