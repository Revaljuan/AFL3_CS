# script4_dict_attack.py
import hashlib
import os

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

if __name__ == "__main__":
    PIN_TARGET_MD5 = "0110b96270248f746ecca06f1ce09746"  # target hash (same as #1)
    pinlist_path = os.path.join(os.path.dirname(__file__), "pinlist.txt")
    print("Script 4 - Dictionary attack using pinlist.txt")
    print("Looking for PIN whose MD5 equals", PIN_TARGET_MD5)
    if not os.path.exists(pinlist_path):
        print("pinlist.txt not found at", pinlist_path)
        print("Create pinlist.txt with candidates (one per line) and rerun the script.")
    else:
        found = []
        with open(pinlist_path, 'r') as f:
            for line in f:
                pin = line.strip()
                if not pin:
                    continue
                if md5(pin) == PIN_TARGET_MD5:
                    found.append(pin)
        if found:
            print("Found matching PIN(s):", found)
        else:
            print("No matching PIN found in pinlist.txt")
