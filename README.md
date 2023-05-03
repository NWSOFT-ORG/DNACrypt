# DNACrypt
> Encrypt files into DNA chromosomes! 🧬

## Introduction
This project can:
- Read/Write DNACrypt Key files
    - Generate Key files
- Encrypt/Decrypt Files

## Encryption/Decryption Procedure
### Encryption
1. Read the file and key file
2. Parse every key
3. Shift every byte in the file with the corresponding key
4. Transform every byte into `AT` or `GC`
5. Add random bytes
6. Write to file

### Decryption
1. Read the file and key file
2. Discard random bytes
3. parse the remaining DNA bytes into numbers
4. Parse every key
5. Un-shift each byte with the corresponding key
6. Write to file

## Key Generation/Parsing
### Generation
1. Generate `n` random integers from 0 to 10
2. Transform each of the integers, `i` to `i` 0s and `10 - i` 1s
3. Transform each 0 to `AT` and 1 to `GC`
4. Add random bytes and a version header
5. Write to a key file
### Parsing
1. Read the key file
2. Discard random bytes
3. Transform each `AT` to 0 and `GC` to 1
4. Transform the Os and 1s to a binary string , then convert to decimal

## Licensing
This project is licensed under the MIT License
