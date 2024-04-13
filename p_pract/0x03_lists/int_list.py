#!/usr/bin/python3

def print_list_int(my_list=[]):
    for value_list in my_list:
        print(f"{value_list}")

def element_at(my_list, idx):
    return(my_list[idx])

def  replace_in_list(mylist, idx, element):
    mylist[idx] = element
    return(mylist)

def print_reverse(my_list=[]):
    len_list = len(my_list)
    for num in reversed(range(0, len_list)):
        print(f"{my_list[num]}")

def no_c(my_string):
    index = 0
    list_to_string = ""
    string_list = list(my_string)
    for char_s in string_list:
        if char_s == 'c':
            del string_list[index]
        index += 1
    for char_s in string_list:
        list_to_string = list_to_string + char_s
    return(list_to_string)

def add_tuple(tuple_a=(), tuple_b=()):
    value_a = tuple_a[0] + tuple_b[0]
    value_b = tuple_a[1] + tuple_b[1]
    new_ab = (value_a, value_b)
    return (new_ab)

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_character = "None"
    else:
        string_list = list(sentence)
        first_character = string_list[0]
    return length, first_character

def max_integer(my_list=[]):
    index = 0
    for value in my_list:
        if index == 0:
            max_value = value
            index = 1
        elif value >= max_value:
            max_value = value
    return max_value

def delete_at(my_list=[], idx=0):
    length = len(my_list)
    del_list = my_list
    print(length)
    if idx < length and idx > 0:
        del del_list[idx]
    return del_list

