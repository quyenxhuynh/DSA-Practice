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
    
    def contains(self, value):
        if size == 0:
            return False
        it = self.head.next
        while it.hasNext():
            if it.value == value:
                return True
        return False
    
    def remove(self):
        if size == 0:
            return
        temp = self.head.next.value
        self.head.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return temp
    
    def removeFirst(self):
        return self.remove()
    
    def removeLast(self):
        if size == 0: 
            return
        temp = self.tail.prev.value
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return temp
    
    def removeIndex(self, index):
        if index > self.size:
            return
        it = self.head.next
        for i in range(index):
            it = it.next
        temp = it.value
        it.prev.next = it.next
        it.next.prev = it.prev
        self.size -= 1
        return temp
    
    def removeItem(self, value):
        if self.size == 0:
            return False
        it = self.head.next
        while it.hasNext():
            if it.value == value:
                it.prev.next = it.next
                it.next.prev = it.prev
                return True
            it = it.next
        return False
    
    def poll(self):
        return self.remove()
    
    def pollFirst(self):
        return self.remove()
    
    def pollLast(self):
        return self.removeLast()

    def indexOf(self, value):
        if size == 0: 
            return
        i = 0
        it = self.head.next
        while it.hasNext():
            if it.value == value:
                return i
            i += 1
            it = it.next
        return -1
    
    def setIndex(self, index, value):
        if index > self.size:
            return
        it = self.head.next
        for i in range(index):
            it = it.next
        it.value = value
        return
    
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
    
    def peek(self):
        return self.getFirst()
    
    def peekFirst(self):
        return self.getFirst()
    
    def peekLast(self):
        return self.getLast()
    
    def pop(self):
        return self.removeFirst()

    def push(self):
        return self.addFirst()
    
    def offer(self, value):
        return self.addLast(value)
    
    def offerFirst(self,value):
        return self.addFirst(value)
    
    def offerLast(self,value):
        return self.addLast(value)

    def size(self):
        return self.size
    
    def toList(self):
        lst = []
        it = self.head.next
        while it.hasNext():
            lst.append(it.value)
            it = it.next
        return lst
    
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
    
