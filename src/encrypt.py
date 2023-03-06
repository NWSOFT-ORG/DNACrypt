from typing import List

from NWSh.printing import print_error

from src.dna_bin import encode_dna
from src.key import parse_keys


def encrypt(key: bytes, string: bytes) -> List[bytes]:
    data = parse_keys(key)
    keys = data[1:] * 2  # Make sure that the key is longer than the data

    enc_bytes = []
    for index, byte in enumerate(string):
        code = byte
        code += keys[index]
        enc_charcode = bin(code)[2:]
        enc_charcode = encode_dna(enc_charcode)
        enc_bytes.append(enc_charcode)
    return enc_bytes
