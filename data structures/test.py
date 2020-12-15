import doubly_linked_list

node = doubly_linked_list.Node(1)
assert(node.value == 1)
assert(node.next == None)
assert(node.prev == None)

linkedlist = doubly_linked_list.LinkedList()
assert(linkedlist.size == 0)