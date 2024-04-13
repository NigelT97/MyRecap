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
    for char_s in my_string:
        if char_s == "c":
            del my_string[index]
        index += 1
    return(my_string)

