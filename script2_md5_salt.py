# script2_md5_salt_prefix.py
import hashlib

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

if __name__ == "__main__":
    PIN = "202345"
    target = "8d4c531eb4b0f54df72aa6839abbeaec"
    found = None
    for s in map(str, range(10)):  # '0'..'9'
        h = md5(s + PIN)
        if h == target:
            found = s
            break
    print("Script 2 - MD5(salt || PIN) brute-force (salt prefix)")
    print("PIN:", PIN)
    print("Target MD5:", target)
    if found is not None:
        print("Found salt:", found)
        print("Verification MD5('{}'+PIN) =".format(found), md5(found + PIN))
    else:
        print("No 1-digit salt found that matches target.")
