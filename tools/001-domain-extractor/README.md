# Domain Extractor

Extract unique domain names from text files such as emails, logs, or notes.

This is a small utility meant for quick IOC extraction during phishing analysis or log review.

## Usage

```bash
./extract_domains.py input.txt

**Example**
$ cat sample.txt
Visit https://sub.example.com and http://TEST.com

$ ./extract_domains.py sample.txt
example.com
sub.example.com
test.com

**Notes**

[*]Domains are normalized to lowercase

[*]Duplicates are removed automatically

[*]Designed to be simple, fast, and dependency-free

**Context**
This tool is part of Cyber2026 — a daily commitment to building small, useful cybersecurity tools.
