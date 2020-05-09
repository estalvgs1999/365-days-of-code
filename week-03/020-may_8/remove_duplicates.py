# ---------------------------------------
#                  DAY 20
#         Coding Interview Question
#
#           REMOVE DUPLICATES
#  Write code to remove duplicates from
#  an unsorted linked list.
#  
#  Question 2.1 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

import sys
sys.path.insert(0, "/home/estalvgs1999/Documentos/code skills/CI02-Project-365/data_structures/linked_list")
import linked_list as LL

# Remove duplicates from an unsorted linked list
# Complexity => O(n); n = list.length
def remove_duplicates(_list):

    item_set = []
    p_node = None
    c_node = _list.head()

    while c_node:

        if c_node.data in item_set:
            p_node.set_next(c_node.next)
        else:
            item_set.append(c_node.data)
            p_node = c_node
        c_node = c_node.next


def test_list():

    l_list = LL.Linked_List()

    # create [1,2,3,4,2,8,2]
    l_list.add(1)
    l_list.add(2)
    l_list.add(3)
    l_list.add(4)
    l_list.add(2)
    l_list.add(8)
    l_list.add(2)

    return l_list


if __name__ == "__main__":
    
    # Test 1
    l_list = test_list()
    l_list.show()
    remove_duplicates(l_list)
    l_list.show()

