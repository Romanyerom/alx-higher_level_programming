#!/usr/bin/python3

def uppercase(s):
    uppercase_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string

input_string = input("Enter a string: ")
result = uppercase(input_string)
print("Uppercase string: {}".format(result))
