#!/usr/bin/python3

output = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        output += chr(i)

print("{}".format(output))
