#!/usr/bin/python3

for i in range(122, 96, -1):
    print("{:c}".format(i), end="")
    if i - 1 >= 97:
        print("{:c}".format(i - 33), end="")
print()

