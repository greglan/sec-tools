#!/usr/bin/env python
import hexdump
import sys

XOR_KEY = 0x12

# Read the input file
fi = open(sys.argv[1], 'rb')
shellcode = '0x'+hexdump.dump(fi.read(),sep='0x').lower()
shellcode_len = len(shellcode) / 4 # '\x' characters, and two digits per byte.
fi.close()

xored_shellcode = ""
i=0
while i < len(shellcode):
    hex_num =int(shellcode[i:i+4], 16)  # 4 characters converted as hex number
    new_hex = hex_num^XOR_KEY
    if new_hex == 0:
        raise Exception("A null byte was created...")
    xored_shellcode += hex(new_hex)+','
    XOR_KEY += 1
    i += 4

xored_shellcode = xored_shellcode[:-1]  # Remove last comma

# Dump the string in a new file
fo = open(sys.argv[1]+".xored.shellcode", 'w')
for c in xored_shellcode:
    fo.write(c)
fo.write('\n')
fo.write(str(shellcode_len))
fo.close()

# Display the shellcode string
print('Crypted shellcode: '+xored_shellcode)
print('Size of the crypted shellcode: '+str(shellcode_len)+" bytes.")
