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
# assert(linkedlist.get(2) == 2)

# for i in range(-1,-5,-1):
#     linkedlist.addFirst(i)

# print(linkedlist)

# linkedlist.addIndex(0,100)
# print(linkedlist)
# assert(linkedlist.getFirst() == 100)
# assert(linkedlist.getLast() == 4)


#############################
####### SINGLY LINKED #######
#############################

import singly_linked_list

node = singly_linked_list.Node(1)
assert(node.value == 1)
assert(node.next == None)

sll = singly_linked_list.LinkedList()
# for i in range(1,10):
#     sll.addFront(i)

# for i in range(10):
#     sll.addEnd(i)

