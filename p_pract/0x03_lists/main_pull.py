#!/usr/bin/python3

import int_list
import random

if __name__ == "__main__":
    my_list5 = [1, 2, 3, 5]
    string_given = "My school is lock"
    index = random.randrange(0, 3)
    value_index = random.randrange(5, 19)

    old_list = my_list5[:]

    int_list.print_list_int(my_list5)

    value_taken = int_list.element_at(my_list5, index)

    print(f"Element at index {index} is {value_taken}")
    
    new_list = int_list.replace_in_list(my_list5, index, value_index)

    print(my_list5)
    print(new_list)
    print(old_list)

    int_list.print_reverse(new_list)

    print(int_list.no_c(string_given))




