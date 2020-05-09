# ---------------------------------------
#  NODE FOR DS
#  by: @estalvgs1999
# ---------------------------------------

# Data Structures Node
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node