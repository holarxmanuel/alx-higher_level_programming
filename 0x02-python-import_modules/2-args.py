#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{:d} argument{}".format(argv_len, 's' if argv_len != 1 else ''), end='')
    print(':' if argv_len > 0 else '.')

    for idx, arg in enumerate(args, start=1):
        print("{:d}: {:s}".format(idx, arg))
