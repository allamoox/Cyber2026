#!/usr/bin/env python3
import re
import sys

DOMAIN_REGEX = r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b"

def extract_domains(text: str):
    return sorted(set(re.findall(DOMAIN_REGEX, text.lower())))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_domains.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    for d in extract_domains(content):
        print(d)
