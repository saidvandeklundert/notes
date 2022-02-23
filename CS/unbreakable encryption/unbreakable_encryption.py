"""
1.3
Encrypting data with dummy data and ensure that the dummy data can be decrypted.

The dummy data must:
- be the same length as the original data
- be random
- and the keys must be truly secret
"""
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # generte length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")  # big endian


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")

    return temp.decode()


if __name__ == "__main__":
    print(random_key(100))
    print(random_key(150))
    print(encrypt("YOLOCOLO"))
    key1, key2 = encrypt("One time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
