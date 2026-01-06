# URL Obfuscator / Deobfuscator
A small blue-team utility to **obfuscate** URLs for safe sharing (tickets, chats, reports),
and **deobfuscate** common IOC formats back into normal URLs.

## Usage

### Obfuscate
```bash
./url_obfuscator.py --obfuscate input.txt

### Deobfuscate
```bash
./url_obfuscator.py --deobfuscate input.txt

# What it handles

###Deobfuscate:

hxxp:// → http://
hxxps:// → https://
example[.]com → example.com


###Obfuscate:

http:// → hxxp://
https:// → hxxps://
Dots inside URL tokens become [.]

###Context
Part of **Cyber2026** initiative, one useful cybersecurity tool or idea per commit. Where I want to Learn programming by reinventing the wheel, breaking it, and rebuilding it.

Yes, it’s manual. Yes, it’s on purpose.

Coding, failing, and understanding what’s actually happening. Thank You Gizmore!
