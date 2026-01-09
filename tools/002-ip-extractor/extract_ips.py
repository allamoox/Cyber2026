#!/usr/bin/env python3
import re
import sys

IP_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

def extract_ips(text: str):
    return sorted(set(re.findall(IP_REGEX, text)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_ips.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    for ip in extract_ips(content):
        print(ip)
