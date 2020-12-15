# based on java's methods
# https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html

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
    
    def add(self, value):
        new_node = Node(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def addIndex(self, index, value):
        new_node = Node(value)
        it = self.head.next
        for i in range(index):
            it = it.next
        new_node.next = it
        new_node.prev = it.prev
        it.prev.next = new_node
        it.prev = new_node
        self.size += 1
    
    def addLast(self, value):
        new_node = Node(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def addFirst(self, value):
        new_node = Node(value)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
    
    def remove(self):
        if size == 0: 
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
    
    def removeIndex(self, index):
        if index > self.size:
            return
        it = self.head.next
        for i in range(index):
            it = it.next
        it.prev.next = it.next
        it.next.prev = it.prev
        self.size -= 1
    
    def get(self, index):
        if index > self.size:
            return
        it = self.head.next
        for i in range(index):
            it = it.next
        return it.value
    
    def getFirst(self):
        if self.size == 0:
            return
        return self.head.next.value
    
    def getLast(self):
        if self.size == 0:
            return
        return self.tail.prev.value
    
    def size(self):
        return self.size
    
    def __str__(self):
        iterator = self.head.next
        s = "["
        while iterator.hasNext():
            s += str(iterator.value)
            if iterator.next.next != None:
                s += ","
            iterator = iterator.next
        s += "]"
        return s
    
