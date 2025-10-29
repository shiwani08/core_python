import math

def using_args(*args):

    """ Adding a docstring for better understaning """

    sum = 0

    for value in args:
        sum = sum + value
    print("The sum of all arguments is:", sum)

def square_root(num):
    print(f"The sqrt of {num} is: {math.sqrt(num)}")

using_args(1, 2, 3, 4, 5)
square_root(144)