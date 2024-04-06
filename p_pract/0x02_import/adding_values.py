#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv_num = len(sys.argv)
    t_add = 0

    for value in range(1, argv_num):
        t_add += int(sys.argv[value])
    print(t_add)