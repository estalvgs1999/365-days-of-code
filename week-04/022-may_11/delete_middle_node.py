# ---------------------------------------
#                  DAY 22
#         Coding Interview Question
#
#           DELETE MIDDLE NODE
#  Implement an algorithm to delete a
#  node in the middle (i.e., any node but
#  the first and last node, not necessa-
#  rily the exact middle) of a singly
#  linked list, given only access to
#  that node.
#  
#  Question 2.3 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# This algorithm is the isolated case of a node that is 
# neither the first nor the last.
def delete_node(node):

    if node == None or node.next == None:
        return False
    
    nxt_node = node.next
    node.data = nxt_node.data
    node.next = nxt_node.next
    return True


