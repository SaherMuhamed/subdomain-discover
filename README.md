# Website Subdomain Discover
This is a Python script that scans for subdomains of a target website using a wordlist of domain names.

## Table of Contents
- <a href="https://github.com/SaherMuhamed/subdomain-discover#description">Description</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#requirements">Requirements</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#usage">Usage</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#options">Options</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#example">Example</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#screenshots">Screenshots</a>
- <a href="https://github.com/SaherMuhamed/subdomain-discover#description">Key Features</a>

## Description
The Subdomain Scanner is a simple Python script that takes a target URL and a wordlist of domain names as input. It then appends each word in the wordlist to the target URL to create potential subdomains and sends HTTP requests to check if these subdomains are valid. If a subdomain responds with a successful HTTP status code (2xx), it is considered a discovered subdomain, and its details are printed to the console.

## Requirements
- Python 3.x
- requests library (can be installed using `pip install requests`)

## Usage
To run the Subdomain Scanner, use the following command format:
```commandline
python3 subdomain_crawler.py -u <target_url> -w <wordlist_file>
```

## Options
- The Subdomain Scanner supports the following options:
    - `-u, --url`: (required) Specifies the target URL of the website for subdomain scanning.
    - `-w, --wordlist`: (required) Specifies the wordlist file in .txt format containing domain names for subdomain generation.

## Example
- To scan for subdomains of the target website `example.com` using the wordlist `wordlist.txt`, run the following command:
    ```commandline
    python3 subdomain_crawler.py -u example.com -w wordlist.txt
    ```
- The script will then scan the subdomains and display discovered subdomains with their corresponding status codes and response times. The results will also be saved in the specified output file.

## Key Features
1. **Wordlist-Based Subdomain Generation:** The script takes a user-provided wordlist containing domain names and appends each word to the target URL, creating potential subdomains to scan.

3. **HTTP Request Validation:** The Subdomain Scanner sends HTTP requests to the generated subdomains and validates their responsiveness. If a subdomain responds with a successful HTTP status code (2xx), it is considered a discovered subdomain.

5. **Real-Time Display:** During the scanning process, the script displays real-time updates, showing each discovered subdomain along with its status code and response time.

## Screenshots
![](https://github.com/SaherMuhamed/subdomain-discover/blob/master/screenshots/Screenshot%20from%202023-09-20%2014-11-04.png)
