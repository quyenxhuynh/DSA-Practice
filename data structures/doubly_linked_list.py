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
    
    def remove(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
    
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
    
