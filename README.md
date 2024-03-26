# -Network-Information-Toolkit
Python script is a powerful toolkit for network analysis and diagnostics. 
It combines various network utilities like nslookup, dig, nmap, and requests to gather and display information about IP addresses and domain names. Whether you're troubleshooting network issues, researching domains, or just curious about the infrastructure of the internet, this toolkit provides a streamlined way to query DNS records, IP address details, and perform port scanning.

## Features
DNS Lookup using nslookup
Fetch IP address of a domain with dig
Perform port scanning and OS detection on an IP address with nmap
Get detailed IP address information using the ipinfo.io API

## Prerequisites
Before running this script, ensure you have Python 3 installed on your system. Additionally, you need the following packages and tools:

requests library for Python
nmap command-line tool

### Use the following command to install the requests library:

```
pip install requests
```
###For nmap, please refer to the official installation guide at Nmap's website.[https://nmap.org/]

## Installation
### Clone this repository or download the script directly:
```
git clone <repository-url>
```
### Navigate to the script's directory:
```
cd network-information-toolkit
```
## Usage
### To use the script, run it from your terminal or command prompt:
```
python network_info_toolkit.py
```
### When prompted, enter the URL of the domain you want to analyze.

## Output
### The script will display:

+ The server's IP address and DNS records.
+ Port scanning results and potential operating system identification for the given IP address.
+ Detailed information about the IP address, including location, ISP, and more.

## Disclaimer
This script is for educational and research purposes only. Ensure you have permission before scanning networks or IP addresses.

## Contributing
Contributions to improve the script or add new features are welcome. Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.





