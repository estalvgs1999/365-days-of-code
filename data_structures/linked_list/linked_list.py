# ---------------------------------------
#  LINKED LIST
#  by: @estalvgs1999
# ---------------------------------------
from node import *

# Linked_List
class Linked_List():


    # List constructor
    def __init__(self):
        self.__head = None
        self.__length = 0


    # Add a new item to the list
    def add(self, data):

        if not self.__head:
            self.__head = Node(data)
        else:
            tmp = self.__head
        
            while tmp.next:
                tmp = tmp.next
        
            tmp.next = Node(data)
        
        self.__length += 1


    # Add an item to the top of the list
    def add_first(self, data):

        tmp = Node(data)
        tmp.set_next(self.__head)
        self.__head = tmp
        self.__length += 1


    # insert a new item to the list at a given index
    def insert(self, data, index):
        
        if not self.__check_index(index):
            return

        if index == 0:
            return self.add_first(data)

        p_node = None
        c_node = self.__head
        c_index = 0
        
        while c_index != index:
            p_node = c_node
            c_node = c_node.next
            c_index+=1

        tmp = Node(data)
        tmp.set_next(c_node)
        p_node.set_next(tmp)

        self.__length += 1


    # Delete an item given its index
    def remove(self, index):

        if not self.__check_index(index):
            return

        p_node = None
        c_node = self.__head
        c_index = 0
        
        while c_index != index:
            p_node = c_node
            c_node = c_node.next
            c_index+=1
        
        # If the head node is to be removed
        if not p_node:
            self.__head = c_node.next
        
        # If the last/middle node is to be removed from the list
        else:
            p_node.set_next(c_node.next)
        
        self.__length -= 1

        return c_node.data


    # Returns the data stored on certain index
    def get(self, index):
        
        if not self.__check_index(index):
            return

        c_node = self.__head
        c_index = 0

        while c_index != index:
            c_node = c_node.next
            c_index+=1
        
        return c_node.data
        

    # Shows the list
    def show(self):
        
        c_node = self.__head

        while c_node:
            print('[{}]->'.format(c_node.data),end="")
            c_node = c_node.next
        
        print('\n')


    # Returns the length of the list
    def length(self):
        return self.__length

    def head(self):
        return self.__head

    def __check_index(self, index):
        if index >= self.__length or index < 0:
            print('IndexError: list index out of range')
            return False
        return True