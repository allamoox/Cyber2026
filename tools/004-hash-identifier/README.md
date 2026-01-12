cat > README.md <<'EOF'
# Hash Identifier

Quick helper to guess a hash type by **format** and **length**.

This does not crack anything. It just helps you quickly classify what you're looking at during investigations.

## Usage

# Identify one hash:
```bash
./hash_id.py -s d41d8cd98f00b204e9800998ecf8427e

# Identify many hashes from a file:
```bash
./hash_id.py -f sample.txt

### Notes 
- 32 hex can be MD5 or NTLM (same length)
- Supports common Unix formats like $1$, $5$, $6$, plus bcrypt/argon2 prefixes
