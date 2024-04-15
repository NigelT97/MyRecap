#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_string = ""
    x = x + 1
    for x in range(0, x):
        try: 
            list_string = f"{list_string}{my_list[x]}"
        except IndexError:
            break
    print(list_string)
    return (len(list_string))

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    result = True
    return result
        