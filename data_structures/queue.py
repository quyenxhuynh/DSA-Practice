import doubly_linked_list

class Queue:
    def __init__(self):
        self.list = doubly_linked_list.LinkedList()

    def enqueue(self, value):
        self.list.addFirst(value)
    
    def dequeue(self):
        return self.list.removeLast()

    def __str__(self):
        return self.list.__str__()
