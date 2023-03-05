import random

def encode_dna(bin_str: str) -> str:
    dna_str = ""
    for char in bin_str:
        match char:
            case "1":
                bases = "CG"
            case "0":
                bases = "AT"
            case _:
                continue
        if random.random() > 0.5:
            bases = bases[::-1]
        dna_str += bases + " "
    return dna_str


def decode_dna(dna_str: str):
    bases = dna_str.split(" ")
    bin_str = ""
    for item in bases:
        match item:
            case "CG" | "GC":
                bin_str += "1"
            case "AT" | "TA":
                bin_str += "0"
            case _:
                continue
    return bin_str
    
    
if __name__ == "__main__":
    bin_str = input("bin> ")
    print(encode_dna(bin_str))
    print(decode_dna(encode_dna(bin_str)))  # If this doesn't match, there should be an error
