from NWSh.printing import print_error

from src.dna_bin import decode_dna
from src.key import parse_keys


def decrypt(key: bytes, enc_msg: bytes):
    data = parse_keys(key)
    enc_bytes = enc_msg.split(b"\n")
    keys = data[1:] * 2  # Make sure that the key is longer than the data

    dec_bytes = []
    for index, byte in enumerate(enc_bytes):
        code = int(decode_dna(byte), 2)
        code -= keys[index]
        try:
            dec_byte = chr(code)
        except (ValueError, OverflowError):
            print_error("decrypt", "Invalid key, cannot decrypt. Are you sure you used the right key?")
            return
        dec_bytes.append(dec_byte.encode("latin-1"))
    return dec_bytes
