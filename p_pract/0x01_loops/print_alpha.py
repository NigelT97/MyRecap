#!/usr/bin/python3

for number in range(0, 20):
    if number == 0:
        last_result = f"{number:02}"
    else:
        last_result = f"{last_result}, {number:02}"
print(last_result)