from hashlib import sha256
import sys

def digest(stringToHash: str) -> str:
    hashBytes = sha256(stringToHash.encode())
    return hashBytes.hexdigest()

if __name__ == "__main__":
    for args in sys.argv[1:]:
        print(digest(args))