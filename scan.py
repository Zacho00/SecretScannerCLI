'''
"Secret" Scanner CLI Tool
Built in Python
By Zach Thomas
'''
import fire
import re
import logging

#Logging Configuration
logging.basicConfig(filename='my_log.txt', level=logging.DEBUG, format='%(message)s')

#Regular Expresssion Patterns
pwpattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$" #General passwords
pkpattern = r"[0-9a-zA-Z/+]{40}" #Amazon Web Service secret key
apipattern = r"AIza[0-9A-Za-z-_]{35}" #Google API keys
tpattern = r"access_token,production[0-9a-z]{161[0-9a,]{32}$" #Paypal Access Token
xpattern = r"[1-9][0-9]+-[0-9a-zA-Z]{40}" #Twitter Access Token

#Private Key Scan
def pk_scan(file):
    count = 0
    print('\nSearching for potential private keys...')
    with open(file, 'r') as f:
        for line in f:
            match = re.search(pkpattern, line)
            count += 1
            if match:
                print(f"\n--------\nLine: {count}\nText: {match.group()}\n--------")
                logging.info(f"Potential Private Key {match} on line {count}")

#Password Scan
def pw_scan(file):
    count = 0
    print('\nSearching for potential passwords...')
    with open(file, 'r') as f:
        for line in f:
            match = re.search(pwpattern, line)
            count += 1
            if match:
                print(f"\n--------\nLine: {count}\nText: {match.group()}\n--------")
                logging.info(f"Potential Password {match} on line {count}")

#API Key Scan
def api_scan(file):
    count = 0
    print('\nSearching for potential API keys...')
    with open(file, 'r') as f:
        for line in f:
            match = re.search(apipattern, line)
            count += 1
            if match:
                print(f"\n--------\nLine: {count}\nText: {match.group()}\n--------")
                logging.info(f"Potential API Key {match} on line {count}")

#Token Scan(Paypal)
def t_scan(file):
    count = 0
    print('\nSearching for potential tokens...')
    with open(file, 'r') as f:
        for line in f:
            match = re.search(tpattern, line)
            count += 1
            if match:
                print(f"\n--------\nLine: {count}\nText: {match.group()}\n--------")
                logging.info(f"Potential Paypal Token {match} on line {count}")

#Token Scan(Twitter)
def x_scan(file):
    count = 0
    print('\nSearching for potential tokens...')
    with open(file, 'r') as f:
        for line in f:
            match = re.search(xpattern, line)
            count += 1
            if match:
                print(f"\n--------\nLine: {count}\nText: {match.group()}\n--------")
                logging.info(f"Potential Twitter Token {match} on line {count}")

#Run All Scans
def main(file):
    pw_scan(file)
    pk_scan(file)
    api_scan(file)
    t_scan(file)
    x_scan(file)

if __name__ == "__main__":
    fire.Fire()

'''
syntax for terminal:
python scan.py (function) (file)
'''