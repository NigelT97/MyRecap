#!/usr/bin/python3

import function_list as funDef
import random

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    rand_x = random.randrange(0, 10)
    
    nb_print = funDef.safe_print_list(my_list, rand_x)
    print("nb_print: {:d} but the random number choosen is {:d}".format(nb_print, rand_x))

    value = 78
    value2 = "math"

    has_been_print = funDef.safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
    
    has_been_print = funDef.safe_print_integer(value2)
    if not has_been_print:
        print("{} is not an integer".format(value2))

    

