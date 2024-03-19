#!/usr/bin/python3

str = "Herberton School"

cut_str = str[:9]
print(f"{str}{str}{str}\n{cut_str}")

#other way of doing it

print(f"{str * 3}\n{str[:9]}")