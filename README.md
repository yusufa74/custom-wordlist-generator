# Custom Wordlist Generator

This Python script allows you to crawl a website and generate a custom wordlist containing unique words from the site's text. It's a useful tool for penetration testers, bug bounty hunters, and cybersecurity enthusiasts who need to generate wordlists for various testing tools (like `hydra`, `ffuf`, or `dirb`).

## Features

- Crawls websites and extracts words from text on the pages.
- Removes duplicate words.
- Allows users to specify the number of words to be extracted.
- Saves the wordlist to a file (`wordlist`).
- Simple to use with Python.

## Installation

To use the script, you will need Python 3.x installed on your machine.

### Steps to get started:

1. Clone this repository:
   ```bash
   git clone https://github.com/yusufa74/custom-wordlist-generator.git
2. Change into the project directory:
cd custom-wordlist-generator
pip install -r requirements.txt
python3 custom_wordlist.py
 
Enter domain (e.g. example.com): http://testphp.vulnweb.com
Enter maximum number of words you want (e.g. 2000): 15

[+] Crawling http://testphp.vulnweb.com...
This may take a few moments.
[+] Visiting: http://testphp.vulnweb.com
[+] Visiting: http://testphp.vulnweb.com/index.php
[+] Visiting: http://testphp.vulnweb.com/categories.php
[+] Visiting: http://testphp.vulnweb.com/artists.php
[+] Visiting: http://testphp.vulnweb.com/disclaimer.php
[+] Visiting: http://testphp.vulnweb.com/cart.php
[+] Visiting: http://testphp.vulnweb.com/guestbook.php
[+] Visiting: http://testphp.vulnweb.com/AJAX/index.php
[+] Visiting: http://testphp.vulnweb.com/login.php
[+] Visiting: http://testphp.vulnweb.com/userinfo.php
[+] Visiting: http://testphp.vulnweb.com/privacy.php
[+] Visiting: http://testphp.vulnweb.com/Mod_Rewrite_Shop/
[+] Visiting: http://testphp.vulnweb.com/hpp/

[+] Done! Saved 15 words to 'wordlist'.




