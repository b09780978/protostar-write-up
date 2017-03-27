#!/usr/bin/env python
import string

# this program is generate string to calculate return address
text = ""
for c in string.ascii_uppercase:
    text += c*4

print text
