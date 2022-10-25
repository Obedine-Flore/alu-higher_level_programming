#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i == 3 * i:
            print("Fizz")
        elif i == 5 * i:
            print("Buzz")
        elif (i == 3 * i) and (i == 5 * i):
            print("FizzBuzz")
        else:
            print(i)
