# script1_md5_pin.py
import hashlib

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

if __name__ == "__main__":
    PIN = "202345"
    target = "0110b96270248f746ecca06f1ce09746"
    h = md5(PIN)
    print("Script 1 - MD5(PIN) verification")
    print("PIN:", PIN)
    print("Computed MD5:", h)
    print("Target MD5:  ", target)
    print("Match:", h == target)
