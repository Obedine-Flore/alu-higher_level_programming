#!/usr/bin/python3
def print_reversed_list_interger(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
