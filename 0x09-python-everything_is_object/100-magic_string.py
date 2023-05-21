#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    print(magic_string.n)
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")

for i in range(5):
    print(magic_string())