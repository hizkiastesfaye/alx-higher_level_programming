#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n != 101 and n != 113:
        print("{:c}".format(n), end='')
