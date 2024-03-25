#!/usr/bin/python3

import random

number = random.randint(-10, 10)

if number < 0:
    print(f"{number} is negative\n")
elif number == 0:
    print(f"{number} is zero\n")
else:
    print(f"{number} is positive")


num = random.randint(-10000, 10000)

last_digit = num % 10
if num < 0:
    last_digit = 10 - last_digit
if last_digit > 5:
    result_msg = "and is greater than 5"
elif last_digit == 0:
    result_msg = "and is 0"
else:
    result_msg = "and is less than 6 and not 0"
msg1 = f"Last digit of {num} is {last_digit} {result_msg}"
print(msg1)