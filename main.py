import sys

from NWSh.arguments import Arguments
from NWSh.commands import register_command_system
from NWSh.printing import print_error, print_result, print_warning
from NWSh.system import System

from src.constants import VERSION
from src.decrypt import decrypt
from src.encrypt import encrypt
from src.key import random_key

DNACRYPT_PREFERENCES = {
    "name": "DNACrypt",
    "version": f"{VERSION}",
    "description": "Encrypt your text into DNA",  # language=HTML
    "author": "Andy Zhang",
    "license": "GPL",
}


def tui_encrypt():
    arguments = Arguments("encrypt")
    arguments.ask_argument("encFile", "File to encrypt")
    arguments.ask_argument("keyFile", "Encryption key file")
    arguments.ask_argument("outFile", "Output file")
    enc_file = arguments.get_argument("encFile")
    key = arguments.get_argument("keyFile")
    out = arguments.get_argument("outFile")
    try:
        with open(key, "rb") as f:
            key_contents = f.read()
    except FileNotFoundError:
        print_error("encrypt", "Key file not found")
        return
    try:
        with open(enc_file, "r", encoding="latin-1") as f:
            msg = f.read().encode("latin-1")
    except FileNotFoundError:
        print_error("encrypt", "File to encrypt not found")
        return

    encrypted = b"\n".join(encrypt(key_contents, msg))
    with open(out, "wb") as f:
        f.write(encrypted)
    print_result("encrypt", "Encrypted successfully. No one can access the data without the key.")


def tui_gen_key():
    arguments = Arguments("key")
    arguments.ask_argument("noOfKeys", "Number of keys to generate", "int")
    arguments.ask_argument("file", "File name to write keys to")
    no_of_keys = arguments.get_argument("noOfKeys")
    file = arguments.get_argument("file")

    key = f"{VERSION}|15*{no_of_keys}\n".encode()
    for _ in range(no_of_keys + 1):
        key += random_key(15).rstrip()
        key += b"\n"
    with open(file, "wb") as f:
        f.write(key)
    print_result("key", "Keys generated successfully")
    print_warning(
        "key",
        "TREAT YOUR KEYS LIKE PASSWORDS. DO NOT SHARE WITH SOMEONE YOU DO NOT TRUST!",
    )


def tui_decrypt():
    arguments = Arguments("decrypt")
    arguments.ask_argument("encFile", "Encrypted file")
    arguments.ask_argument("keyFile", "Encryption key file")
    arguments.ask_argument("outFile", "Output file")
    enc_file = arguments.get_argument("encFile")
    key_file = arguments.get_argument("keyFile")
    out = arguments.get_argument("outFile")

    try:
        with open(key_file, "rb") as f:
            key_contents = f.read()
    except FileNotFoundError:
        print_error("decrypt", "Key file not found")
        return
    try:
        with open(enc_file, "rb") as f:
            enc_msg = f.read()
    except FileNotFoundError:
        print_error("decrypt", "Encrypted file not found")
        return
    dec_bytes = decrypt(key_contents, enc_msg)
    if dec_bytes is None:
        return
    dec_msg = b"".join(dec_bytes)
    with open(out, "wb") as f:
        f.write(dec_msg)
    print_result("decrypt", dec_msg.decode("latin-1"))


if __name__ == "__main__":
    system = System("dna", DNACRYPT_PREFERENCES)
    register_command_system(system, "encrypt", tui_encrypt)
    register_command_system(system, "decrypt", tui_decrypt)
    register_command_system(system, "genKey", tui_gen_key)
    register_command_system(system, "exit", lambda: sys.exit(0))
    while True:
        system.ask_command()
