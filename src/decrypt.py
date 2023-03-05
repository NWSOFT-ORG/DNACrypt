from src.key import parse_keys
from NWSh.printing import print_error
from src.dna_bin import decode_dna


def decrypt(key, enc_msg):
    data = parse_keys(key)
    dimensions = data[0]
    enc_bytes = enc_msg.split("\n")
    if dimensions[1] < 0.8 * len(enc_bytes):
        print_error("The key is too short. Are you sure this is the right one?")
    keys = data[1:] * 2  # Make sure that the key is longer than the data

    dec_bytes = []
    for index, byte in enumerate(enc_bytes):
        code = int(decode_dna(byte), 2)
        code -= keys[index]
        dec_byte = chr(code)
        dec_bytes.append(dec_byte)
    return dec_bytes
