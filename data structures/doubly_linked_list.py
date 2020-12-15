class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def hasNext(self):
        return self.next != None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def size(self):
        return self.size
    
