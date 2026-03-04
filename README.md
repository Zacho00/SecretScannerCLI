# SecretScannerCLI
## Overview
"scan.py" is a Python-based CLI tool used to search through text files to find "hard-coded secrets". This is accomplished through the use of regular expressions. Specifically, "scan.py" will search for:
- Passwords
- Amazon Web Service Secret Keys
- Google API Keys
- Paypal Access Tokens
- Twitter Access Tokens

*NOTE: For easy testing, I have included secrets.txt which includes cases for all search types.

## Requirements
For this program, the simplest way to make "scan.py" a CLI-based tool was to use Fire. Therefore:  
`pip install fire`

## Guide
After you have installed the prerequisite 'fire', you are ready to go! The syntax you will be using is same as standard for terminal usage. You have six functions you can call:
- `pw_scan` will scan for passwords. 
- `pk_scan` will scan for private keys.
- `api_scan` will scan for API keys.
- `t_scan` will scan for Paypal tokens.
- `x_scan` will scan for Twitter tokens.
- `main` will perform a full scan using all possible searches.

Syntax will folow a simple format:

`python scan.py (function) (file)`

An example input into the terminal would be:

`python scan.py main secrets.txt`

**or**

`python scan.py main C:\secret_folder\secrets.txt`
