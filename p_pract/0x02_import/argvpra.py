#!/usr/bin/python3

import sys

argv_n = len(sys.argv) - 1

msg = f"{argv_n} arguments"

if argv_n == 0:
    msg = f"{msg}."
else:
    msg = f"{msg}:"
    for num in range(1, argv_n + 1):
        msg = f"{msg}\n{num}: {sys.argv[num]}"

 
print(msg)
