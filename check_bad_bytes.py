#!/usr/bin/env python3
import hexdump
import argparse


def byte_to_int(n):
    return int.from_bytes(n, 'big')


def int_to_byte(n):
    return n.to_bytes(1, byteorder='big')



def parse_bytes_list(bytes_str):
    str_list = bytes_str.split(',')
    bytes_list = []

    for byte in str_list:
        bytes_list.append(int(byte, 16))

    return bytes_list

def check(binary, bytes_list):
    i = 0
    for byte in binary:
        if byte in bytes_list:
            print("Byte "+hex(byte)+" detected at "+hex(i))
        i+=1




parser = argparse.ArgumentParser(description='Check if the given binary file' \
                                             'contains a forbidden byte')
parser.add_argument('--bytes', help='path of the input file')
parser.add_argument('--input', help='path of the output file')
args = parser.parse_args()


fi = open(args.input, 'rb')
binary = fi.read()
fi.close();

bytes_list = parse_bytes_list(args.bytes)
check(binary, bytes_list)
