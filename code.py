#!/usr/bin/env python

import os
import sys
from subcode import *

print("Hello, World!")

print os.environ["USER"]
print os.environ["HOME"]

print sys.prefix

x = 1
y = 2
print x + y

a = [ 1, 2, 3 ]

print a[1]
b = a[0]
print b

print("Lets make this messy!!!")

printUser( os.environ["USER"])
printHome( os.environ["HOME"])
