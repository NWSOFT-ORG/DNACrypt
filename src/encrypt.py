from src.key import parse_keys
from typing import List
from src.dna_bin import encode_dna

from NWSh.printing import print_error


def encrypt(key: str, string: str) -> List[int]:
    data = parse_keys(key)
    dimensions = data[0]
    if dimensions[1] < 0.8 * len(string):
        print_error("encrypt", "The key should be longer than 80% of the text")
    keys = data[1:] * 2  # Make sure that the key is longer than the data

    enc_bytes = []
    for index, byte in enumerate(string):
        code = ord(byte)
        code += keys[index]
        enc_charcode = bin(code)[2:]
        enc_charcode = encode_dna(enc_charcode)
        enc_bytes.append(enc_charcode)
    return enc_bytes
