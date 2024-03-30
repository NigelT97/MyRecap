#!/usr/bin/python3

def fizzbuzz():
    """
    Fizz buzz function that prints out
    fizz if divisable by 3
    buzz if divisable by 5
    FizzBuzz if by both

    """

    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            var_num = "FizzBuzz"
        elif num % 5 == 0:
            var_num = "Buzz"
        elif num % 3 == 0:
            var_num = "Fizz"
        else:
            var_num = num

        if num == 1:
            string_var = f"{var_num}"
        else:
            string_var = f"{string_var} {var_num}"

    print({string_var})

fizzbuzz()

