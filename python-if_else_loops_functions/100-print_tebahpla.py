#!/usr/bin/python3
for c in range(ord('z'), ord('a')):
    print('{:c}{:s}".format(c, chr(c-33)), end="")
