import sorting, random

lst = []
for i in range(100):
    lst.append(random.randint(1,100))


bubble = sorting.bubbleSort(lst)
sorted(lst)
assert(bubble == lst)