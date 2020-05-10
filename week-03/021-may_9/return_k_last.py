# ---------------------------------------
#                  DAY 21
#         Coding Interview Question
#
#           RETURN Kth TO LAST
#  Implement an algorithm to find the
#  kth to last element of a singly linked
#  list.
#  
#  Question 2.2 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

import sys, os
file_dir = os.path.dirname(os.path.abspath(__file__))
directory_file = os.path.dirname(os.path.dirname(file_dir))
sys.path.insert(0, directory_file+'/data_structures/linked_list')
import linked_list as LL

def print_k_to_last(_list, k):

    c_node = _list.head()
    index = 0

    while index != k:
        c_node = c_node.next
        index += 1

    ret_list = LL.Linked_List()
    ret_list.set_head(c_node)
    ret_list.show()


    