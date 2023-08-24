#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()  # Use a set to store unique numbers
    result = 0

    for num in my_list:
        if num not in unique_numbers:
            result += num
            unique_numbers.add(num)

    return (result)
