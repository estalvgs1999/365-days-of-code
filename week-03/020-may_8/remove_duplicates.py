# ---------------------------------------
#                  DAY 20
#         Coding Interview Question
#
#           REMOVE DUPLICATES
#  Write code to remove duplicates from
#  an unsorted linked list.
#  FOLLOW UP
#  How would you solve this problem if a
#  temporary buffer is not allowed?
#  
#  Question 2.1 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

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
            print(item_set)
            p_node = c_node
        c_node = c_node.next


# What if a temporary buffer is not allowed?
# Complexity => O(n²) and O(1) in space
def remove_duplicates(_list):

    c_node = _list.head()

    while c_node:
        runner = c_node

        while runner.next:
        
            if runner.data == c_node.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
            c_node = c_node.next


if __name__ == "__main__":
    
    pass

