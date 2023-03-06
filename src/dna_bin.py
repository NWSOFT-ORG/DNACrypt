import random
import os
from NWSh.arguments import Arguments


def encode_dna(bin_str: str) -> bytes:
    dna_str = b""
    for char in bin_str:
        match char:
            case "1":
                bases = b"CG"
            case "0":
                bases = b"AT"
            case _:
                continue
        if random.random() > 0.5:
            bases = bases[::-1] + b" "
            bases += os.urandom(random.randint(1, 12)).lower().replace(b"\n", b"").replace(b"\r", b"")  # Add a random byte
            # Convert the byte to lowercase, so it doesn't get confused with our DNA
        dna_str += bases + b" "
    return dna_str


def decode_dna(dna_str: bytes):
    bases = dna_str.split(b" ")
    bin_str = ""
    for item in bases:
        match item:
            case b"CG" | b"GC":
                bin_str += "1"
            case b"AT" | b"TA":
                bin_str += "0"
            case _:  # If we met a random byte, simply ignore it
                continue
    return bin_str


if __name__ == "__main__":
    test = Arguments("bin")
    test.ask_argument("binStr", "A binary string to encode")
    bin_str = test.get_argument("binStr")
    print(encode_dna(bin_str))
    print(
        decode_dna(encode_dna(bin_str))
    )  # If this doesn't match, there should be an error
