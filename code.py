#!/usr/bin/env python

import os
import sys

print("Hello, World!")
print os.environ["USER"]
print sys.prefix

a = [ 1, 2, 3 ]
print a[1]
b = a[0]

print b
