#!/usr/bin/python3

import int_list
import random

if __name__ == "__main__":
    my_list5 = [1, 2, 3, 5]
    string_given = "My school is locked by crooks"
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


    tuple_a = (1, 89)
    tuple_b = (8, 12)
    new_tuple = int_list.add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    sentence = "At School, I learnt C!"
    an_sentence = ""
    my_other_sentence = "Back"
    sentence_list = [sentence, an_sentence, my_other_sentence]
    for index in sentence_list:
        length, first = int_list.multiple_returns(index)
        print("Length: {:d} - First Character: {}".format(length, first))
    
    my_list7 = [-13, -88, 90, 9, 98, -8, 100, 55, 101]
    max_value = int_list.max_integer(my_list7)
    print(max_value)
    idx = 6
    new1_list = int_list.delete_at(my_list7, idx)
    print(new1_list)



