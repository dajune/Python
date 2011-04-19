#!/usr/bin/python
# Filename: macgen.py
# Usage: It's intended to generate MAC addresses for virtualized
#        systems that created by Xen, OpenVZ, Vserver etc.

import random

# The first line is defined for specified vendor
mac = [ 0x00, 0x24, 0x81,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

print ':'.join(map(lambda x: "%02x" % x, mac))
