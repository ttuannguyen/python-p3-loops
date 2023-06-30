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
    for i in range(1, 101):
        # note: place the % 3 and % 5 conditional first because otherwise it's going hit % 3 or % 5 and will not go onto the next line
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)




# Method 2:
# def fizzbuzz():
#     for i in range(1, 101):
#         if not i % 15:
#             print("FizzBuzz")
#         elif not i % 5:
#             print("Buzz")
#         elif not i % 3:
#             print("Fizz")
#         else:
#             print(i)

fizzbuzz()