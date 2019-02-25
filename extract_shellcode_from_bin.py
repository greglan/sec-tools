#!/usr/bin/env python
import hexdump
import argparse


def bin_to_C(binary):
    c_string = 'char shellcode[] = "\\x' + \
    hexdump.dump(binary,sep='\\x').lower() + '";'
    print("\nShellcode as C string:\n" + c_string + "\n")
    return c_string


def bin_to_asm(binary):
    asm_data = 'db 0x'+hexdump.dump(binary, sep=', 0x').lower()
    print("\nShellcode as ASM:\n" + asm_data + "\n")
    return asm_data


parser = argparse.ArgumentParser(description='Extract shellcode strings')
parser.add_argument('path', metavar='binary',
                    help='path of the binary to extract the shellcode from')

args = parser.parse_args()


# Read the input file
fi = open(args.path, 'rb')
binary = fi.read()
fi.close()

bin_to_C(binary)
bin_to_asm(binary)

print("Length: " + hex(len(binary)) + " bytes")
