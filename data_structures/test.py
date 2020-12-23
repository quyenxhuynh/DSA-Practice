#############################
####### DOUBLY LINKED #######
#############################

# import doubly_linked_list

# node = doubly_linked_list.Node(1)
# assert(node.value == 1)
# assert(node.next == None)
# assert(node.prev == None)

# linkedlist = doubly_linked_list.LinkedList()
# assert(linkedlist.size == 0)

# for i in range(0,10):
#     linkedlist.add(i)
# print(linkedlist)
# assert(linkedlist.size == 10)

# for i in range(5):
#     linkedlist.remove()
# print(linkedlist)
# assert(linkedlist.size == 5)
# assert(linkedlist.get(2) == 7)

# linkedlist.addIndex(0,100)
# assert(linkedlist.get(0) == 100)
# assert(linkedlist.getFirst() == 100)
# assert(linkedlist.getLast() == 9)
# print(linkedlist)

# assert(linkedlist.remove() == 100)
# assert(linkedlist.get(0) == 5)
# print(linkedlist)

# assert(linkedlist.removeFirst() == 5)
# assert(linkedlist.get(0) == 6)
# assert(linkedlist.removeLast() == 9)
# assert(linkedlist.getLast() == 8)


#############################
####### SINGLY LINKED #######
#############################

# import singly_linked_list

# node = singly_linked_list.Node(1)
# assert(node.value == 1)
# assert(node.next == None)

# sll = singly_linked_list.LinkedList()
# for i in range(10):
#     sll.addFront(i)

# for i in range(10):
#     sll.addEnd(i)

# for i in range(10):
#     print(sll.getIndex(i))

# for i in range(10):
#     assert(sll.contains(i) == True)

# print(sll)
# sll.removeTail()
# print(sll)


#############################
########### STACK ###########
#############################
# import stack

# stack = stack.Stack()
# for i in range(10):
#     stack.push(i)

# for i in range(10):
#     stack.pop()


#############################
########### QUEUE ###########
#############################
# import queue

# queue = queue.Queue()
# for i in range(10):
#     queue.enqueue(i)

# for i in range(10):
#     assert(queue.dequeue() == i)
