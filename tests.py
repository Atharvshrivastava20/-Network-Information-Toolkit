import subprocess
import requests
import json

def get_ip_info(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    ip_info = json.loads(response.text)
    return ip_info

def run_nslookup(url):
    result = subprocess.run(['nslookup', url], capture_output=True, text=True)
    print(result.stdout)

def run_dig(url):
    result = subprocess.run(['dig', '+short', url], capture_output=True, text=True)
    ip_address = result.stdout.strip()
    print(f'IP address of {url}: {ip_address}')
    return ip_address

def run_nmap(ip_address):
    result = subprocess.run(['sudo', 'nmap', '-O', ip_address], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'Error running nmap: {result.stderr}')
    else:
        print(result.stdout)

def main():
    url= input("please enter a url")
    run_nslookup(url)
    ip_address = run_dig(url)
    run_nmap(ip_address)

    ip_info = get_ip_info(ip_address)
    print(json.dumps(ip_info, indent=4))
 
   

if __name__ == "__main__":
    main()