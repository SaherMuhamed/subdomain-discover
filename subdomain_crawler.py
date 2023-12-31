import sys
from art import subdomain_art
import urllib3
import requests
from argparse import ArgumentParser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}  # It will send the request like browsers

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write(
        "Please update and make sure you use the command python3 subdomain_crawler.py -u <url> -w <wordlist>\n\n")
    sys.exit(0)


def args():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", dest="target_url", help="Enter URL you want to test. Example: -u example.com")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="Choose the wordlist file. Example: -w common.txt")
    options = parser.parse_args()
    if not options.target_url:
        parser.error("[-] Please specify website url, or type it correctly, ex: -u example.com")
    elif not options.wordlist:
        parser.error("[-] Please specify a wordlist file, or type it correctly, ex: -w common.txt")
    return options


def request(website_url):
    try:
        return requests.get(url="http://" + website_url, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        pass


def main():
    print(subdomain_art)
    try:
        with open(file=args().wordlist, mode="r") as file:
            for line in file:
                test_url = line.strip() + "." + args().target_url
                response = request(website_url=test_url)
                if response:
                    print("[+] Discovered Subdomain ==> http://" + test_url + " | Status Code " + str(
                        response.status_code) + " | TTL " + str(
                        round(response.elapsed.microseconds * 0.001, 2)) + " ms")  # print detailed info
                sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n[*] Detected 'ctrl + c' pressed, program terminated.")
        sys.exit(0)


if __name__ == "__main__":
    main()
