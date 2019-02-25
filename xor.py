#!/usr/bin/env python3
import hexdump
import argparse


def byte_to_int(n):
    return int.from_bytes(n, 'big')


def int_to_byte(n):
    return n.to_bytes(1, byteorder='big')


def encryption(binary, key):
    n = len(binary)
    i = 0
    xored_binary = b''

    while i < n:
        new_hex = binary[i] ^ key
        if new_hex == b'\x00':
            raise Exception("A null byte was created !")
        xored_binary += int_to_byte(new_hex)
        i += 1
    return xored_binary


parser = argparse.ArgumentParser(description='XOR a binary with the given key')
parser.add_argument('--input', help='path of the input file')
parser.add_argument('--output', help='path of the output file')
parser.add_argument('--key', help='XOR key to use', type=int)
args = parser.parse_args()


fi = open(args.input, 'rb')
binary = fi.read()
fi.close();

xored_binary = encryption(binary, args.key)

fo = open(args.output, 'wb')
fo.write(xored_binary)
fo.close()
