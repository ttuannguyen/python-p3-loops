#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    # since this is a reverse loop
    # the range is 10 to 0 but not incl. 0
    # the 3rd parameter states specifies the decrementing value with -1
    while i in range(10, 0, -1):
        print(i)
        i -= 1 
    print("Happy New Year!")




# Method 1
# def square_integers(int_list):
#     result = list()
#     for integer in int_list:
#         square_integer = integer * integer 
#         result.append(square_integer) 
#     return result

# Method 2
def square_integers(int_list):
    result = [integer * integer for integer in int_list]
    return result

# print(square_integers([1, 2, 3, 4, 5]))


def fizzbuzz():
    for i in range(10):
        print(i)

fizzbuzz()