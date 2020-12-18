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
        return
    
    def addEnd(self, value):
        return
       
    def __str__(self):
        s = "["
        it = self.head.next
        while it.next:
            s += str(it.value)
            if it.next.next:
                s += ","
            it = it.next
        s += "]"
        return s

