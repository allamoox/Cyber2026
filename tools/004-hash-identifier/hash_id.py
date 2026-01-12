#!/usr/bin/env python3
import argparse
import re
import sys

HEX_RE = re.compile(r"^[0-9a-fA-F]+$")

def identify_hash(s: str) -> str:
    h = s.strip()
    if not h:
        return "empty"

    if h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$"):
        return "bcrypt (Blowfish)"
    if h.startswith("$argon2"):
        return "argon2"
    if h.startswith("$6$"):
        return "sha512crypt (Unix)"
    if h.startswith("$5$"):
        return "sha256crypt (Unix)"
    if h.startswith("$1$"):
        return "md5crypt (Unix)"

    if not HEX_RE.match(h):
        return "unknown (not pure hex / not a common prefix format)"

    n = len(h)

    if n == 32:
        # Both MD5 and NTLM are 32 chars
        return "MD5 or NTLM (both are 32 hex)"
    if n == 40:
        return "SHA-1"
    if n == 56:
        return "SHA-224"
    if n == 64:
        return "SHA-256"
    if n == 96:
        return "SHA-384"
    if n == 128:
        return "SHA-512"

    return f"unknown (hex length {n})"


def main() -> int:
    p = argparse.ArgumentParser(
        description="Inhouse hash type identifier by format/length.",
        epilog=(
            "Examples:\n"
            "  ./hash_id.py -s d41d8cd98f00b204e9800998ecf8427e\n"
            "  ./hash_id.py -f sample.txt\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("-s", "--string", help="Hash string to identify")
    g.add_argument("-f", "--file", help="Text file with hashes (one per line)")
    args = p.parse_args()

    items = []
    if args.string:
        items = [args.string]
    else:
        try:
            with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
                items = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"File not found: {args.file}")
            return 1

    for h in items:
        print(f"{h}  ->  {identify_hash(h)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
