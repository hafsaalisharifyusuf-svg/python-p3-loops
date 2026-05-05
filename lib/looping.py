#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")
    
    # code goes here!
    pass


def square_integers(int_list):
    result = []
    for num in int_list:
        result.append(num * num)
    return result

    # code goes here!
    pass
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    # code goes here!
    pass