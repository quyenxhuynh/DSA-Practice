import singly_linked_list

class Stack:
    def __init__(self):
        self.list = singly_linked_list.LinkedList()

    def push(self, value):
        self.list.addFront(value)
    
    def pop(self):
        return self.list.removeHead()
    
    def isEmpty(self):
        return self.list.size == 0
    
    def __str__(self):
        return self.list.__str__()