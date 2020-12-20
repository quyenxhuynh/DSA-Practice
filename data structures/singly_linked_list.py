class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0
    
    def addFront(self, value):  
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addIndex(self, index, value):
        if index > self.size + 1:
            return
        new_node = Node(value)
        it = self.head
        for i in range(index):
            it = it.next
        new_node.next = it.next
        it.next = new_node
        self.size += 1
    
    def addEnd(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head.next = new_node
        else: 
            it = self.head.next
            for i in range(self.size-1):
                it = it.next
            it.next = new_node
        self.size += 1
    
    def contains(self, value):
        it = self.head.next
        for i in range(self.size):
            if it.value == value:
                return True
            it = it.next
        return False
    
    def getValue(self, index):
        if index > self.size or index < 0:
            return
        i = 0
        it = self.head.next
        for i in range(index):
            it = it.next
        return it.value
    
    def getIndex(self, value): # first occurrence of value
        it = self.head.next
        for i in range(self.size):
            if it.value == value:
                return i
            it = it.next
        return -1
    
    def removeHead(self):
        it = self.head.next
        self.head = it.next
        it.next = None
       
    def __str__(self):
        s = "["
        it = self.head.next
        for i in range(self.size):
            s += str(it.value)
            if i != self.size - 1:
                s += ","
            it = it.next
        s += "]"
        return s

