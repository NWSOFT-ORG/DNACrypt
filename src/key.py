import random
from typing import List

from NWSh.printing import print_error

from src.constants import VERSION
from src.dna_bin import encode_dna


def random_key(length: int) -> bytes:
    zeros = random.randint(1, int(length * 0.75))
    key = ""
    key += "0" * zeros
    key += "1" * (length - zeros)

    key = "".join(random.sample(key, length))  # Shuffle the 0s and 1s
    key = encode_dna(key)
    return key


def get_encrypt_number(key: bytes) -> int:
    a = key.count(b"0")
    b = len(key) - a
    number = a**b + b**a - a * b + b - a
    return number


def parse_keys(keys: bytes) -> List[int]:
    lines = keys.splitlines()

    info_line = lines[0]
    info = info_line.split(b"|")
    ver = float(info[0])
    if int(ver) != int(VERSION):
        print_error("genKey", "Incompatible version")
    dimensions = [int(x) for x in info[1].split(b"*")]

    # Empty byte at bottom
    keys_list = lines[1:-1]
    return [tuple(dimensions), *[get_encrypt_number(key) for key in keys_list]]
