# script3_md5_kdf3_salt_prefix.py
import hashlib

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

if __name__ == "__main__":
    PIN = "202345"
    target = "b20f8b0405b88e2b0b50eb3356d34ba7"
    found = None
    for s in map(str, range(10)):  # '0'..'9'
        h0 = s + PIN            # salt || PIN (string)
        h1 = md5(h0)
        h2 = md5(h1)
        h3 = md5(h2)
        if h3 == target:
            found = s
            break

    print("Script 3 - MD5^3(salt || PIN) brute-force (salt prefix)")
    print("PIN:", PIN)
    print("Target MD5^3:", target)
    if found is not None:
        print("Found salt:", found)
        # show intermediate values
        h0 = found + PIN
        h1 = md5(h0)
        h2 = md5(h1)
        h3 = md5(h2)
        print("h0 (salt+PIN):", h0)
        print("h1 = md5(h0):", h1)
        print("h2 = md5(h1):", h2)
        print("h3 = md5(h2):", h3)
    else:
        print("No 1-digit salt found that matches target after 3 iterations.")
