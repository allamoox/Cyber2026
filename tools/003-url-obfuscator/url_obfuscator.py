#!/usr/bin/env python3
import argparse
import re
import sys

URL_REGEX = re.compile(r"\b(?:h..ps?|https?)://\S+\b", re.IGNORECASE)


def deobfuscate(text: str) -> str:
    text = re.sub(r"\bhxxps://", "https://", text, flags=re.IGNORECASE)
    text = re.sub(r"\bhxxp://", "http://", text, flags=re.IGNORECASE)
    text = re.sub(r"\[\.\]", ".", text)
    text = re.sub(r"\(\.\)", ".", text)
    return text


def obfuscate(text: str) -> str:
    text = re.sub(r"\bhttps://", "hxxps://", text, flags=re.IGNORECASE)
    text = re.sub(r"\bhttp://", "hxxp://", text, flags=re.IGNORECASE)

    def _obf_token(m: re.Match) -> str:
        token = m.group(0)
        return token.replace(".", "[.]")

    return URL_REGEX.sub(_obf_token, text)


def main():
    p = argparse.ArgumentParser(
        description="Obfuscate or deobfuscate URLs in a text file (blue-team safe sharing)."
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--obfuscate", action="store_true")
    g.add_argument("--deobfuscate", action="store_true")
    p.add_argument("file")

    args = p.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: file not found -> {args.file}")
        return 1

    result = obfuscate(content) if args.obfuscate else deobfuscate(content)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
