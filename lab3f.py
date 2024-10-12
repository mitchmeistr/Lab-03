#!/usr/bin/env python3

# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-10-12

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]



def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    add_num = ordered_list[-1]
    add_num = add_num + 1
    ordered_list = ordered_list.append(add_num)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for remove_num in items_to_remove:
        ordered_list.remove(remove_num)


# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)