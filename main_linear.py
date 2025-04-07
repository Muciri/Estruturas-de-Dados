from linear_structures.Stack import Stack
from linear_structures.Queu import Queue
from linear_structures.Deck import Deck
from linear_structures.List import List

print('=-=-=-=-=-=-=-Stack Tests=-=-=-=-=-=-=-')
stack = Stack()

print("empty stack: ",stack)

stack.pile(1)
stack.pile(2)
stack.pile(3)
stack.pile(4)
stack.pile(5)
print("stack with elements: ",stack)

stack.unpile()
stack.unpile()
print("stack with 2 elements less: ",stack)

print("stack's lenght: ", len(stack))
print("stack's 2rd element: ",stack[1])
print("stack's 3rd element: ",stack[2])
print("searching an element:", stack.element(1))
print("searching an non-existent element:", stack.element('error'))

print()
print('=-=-=-=-=-=-=-Queue Tests=-=-=-=-=-=-=-')
file = Queue()
print("empty queue:", file)

file.queue(1)
file.queue(2)
file.queue(3)
file.queue(4)
file.queue(5)
print("queue with elements:", file)

file.dequeue()
file.dequeue()
print("queue with 2 less elements:", file)

print("queue's lengh:",len(file))
print("queue's 2rd element: ",file[2])
print("queue's 3rd element: ",file[2])
print("searching an element: ", file.element(1))
print("searching an non-existent element: ", file.element('error'))

print("queue before reverting it:", file)
file.reverse()
print("queue after reverting it:", file)

print()
print('=-=-=-=-=-=-=-Deck Tests=-=-=-=-=-=-=-')
deck = Deck()
print("empty Deck:", deck)

deck.add_tail(1)
deck.add_tail(2)
deck.add_tail(3)
deck.add_tail(4)
deck.add_tail(5)
print("Deck with added elements in tail:", deck)

deck.add_head(1)
deck.add_head(2)
deck.add_head(3)
deck.add_head(4)
deck.add_head(5)
print("Deck with added elements in head:", deck)

deck.pop_head()
deck.pop_head()
print("Deck with 2 less elements in head:", deck)

deck.pop_tail()
deck.pop_tail()
print("Deck with 2 less elements in tail:", deck)

print("Deck's lengh:",len(deck))
print("Deck's 2rd element: ",deck[2])
print("Deck's 3rd element: ",deck[2])
print("searching an element: ", deck.element(1))
print("searching an non-existent element: ", deck.element('error'))

print("add_tail before reverting it:", deck)
deck.reverse()
print("add_tail after reverting it:", deck)

print()
print('=-=-=-=-=-=-=-List Tests=-=-=-=-=-=-=-')
list = List()
print("empty list:", list)

for i in range(10):
    list.append(i)
print("list with elements:", list)

list.pop(3)
list.pop(0)
print("list with 2 less elements:", list)

print("5rd element of the list: ",list[4])
print("6rd element of the list: ",list[5])

list[3] = 50
print("list with 4rd element modified:", list)

print("list before reverting it: ", list)
list.reverse()
print("list after reverting it: ",list)
print("list's lenght: ", len(list))