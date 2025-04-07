# Data Structures  
This repository contains simple explanations and examples of basic data structures implemented in Python.  
Author: Murilo Maciel Rodrigues - Student of Systems for Internet - IFPB (Instituto Federal da Paraíba) 

---

## Stack  
A **stack** is a LIFO (Last In, First Out) data structure. The last element added is the first one to be removed.  
In Python, stacks can be implemented using lists with the `append()` and `pop()` methods.  
**Use cases**: undo features, expression evaluation, backtracking.

---
## Queue
A **queue** is a FIFO (First In, First Out) data structure. The first element added is the first one removed.
In Python, queues can be implemented using collections.deque or queue.Queue.
Use cases: task scheduling, print queues, buffering.

## Deck
A **deck** (double-ended queue) allows insertion and removal from both ends.
Python’s collections.deque supports operations like append(), appendleft(), pop(), and popleft().

## List
A **linked** list is a collection of nodes where each node contains a value and a pointer to the next node.
Python does not have a built-in linked list, but it can be implemented using custom classes.
Use cases: efficient insertions/deletions, dynamic memory usage.