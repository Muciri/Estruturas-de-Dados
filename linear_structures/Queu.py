from Nodes.Node import Node

class QueueError(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class Queue:
    '''
    Queue Data Structure \n
    ────────────────────────────────────────────────────────────────────── \n
    Queues follow the First In, First Out (FIFO) principle, where the first element added is the first one to be removed. \n
    Queues are commonly used in task scheduling, order processing, and handling requests in the order they arrive. \n
    ────────────────────────────────────────────────────────────────────── \n
    author: Murilo Maciel Rodrigues \n
    Student of Systems for Internet - IFPB (Instituto Federal da Paraíba) 
    '''
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def __str__(self):
        if self.empty():
            return '[]'
        
        string = '[>'
        cursor = self.__head
        while cursor != None:
            string += f'{str(cursor.data)}, '
            cursor = cursor.next
        string = string.rstrip(', ') + '<]'

        return string
    
    def __len__(self):
        return self.__size

    def __gt__(self, other):
        return self.__size > len(other)

    def __lt__(self, other):
        return self.__size < len(other)

    def __ge__(self, other):
        return self.__size >= len(other)

    def __le__(self, other):
        return self.__size <= len(other)
    
    def head(self):
        '''returns the head of the queue'''
        return self.__head
    
    def tail(self):
        '''returns the tail of the queue'''
        return self.__tail
    
    def empty(self):
        '''returns True if the queue is empty, otherwise returns False'''
        return self.__size == 0
    
    def queue(self, data:any):
        '''adds a new element to the queue'''
        new_element = Node(data)
        if self.empty():
            self.__head = self.__tail = new_element
        else:
            self.__tail.next = new_element
            self.__tail = new_element
        self.__size += 1
    
    def dequeue(self):
        '''removes the head element to the queue if it is not empty and returns the element'''
        if self.empty():
            raise QueueError('the queue is already empty')
        element = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return element
    
    def reverse(self):
        '''reverts the queue'''
        for i in range(self.__size-1, -1, -1):
            self.queue(self[i])
        for _ in range(int(self.__size/2)):
            self.dequeue()
    
    def element(self, key:any):
        '''searchs an element from the queue by its key. if the method can not find the element, it returns None'''
        cursor = self.__head
        while cursor != None:
            if cursor.data == key:
                return cursor.data
            cursor = cursor.next
        return None

    def index(self, key:any):
        '''searchs the index value of an element from the Stack by its key. if the method can not find the element, it returns None'''
        cursor = self.__head
        cont = 0
        while cursor != None:
            if cursor.data == key:
                return cont
            cursor = cursor.next
            cont +=1
        return None

    def __getitem__(self, key:int):
        '''special method to acess elements in the stack by their index'''
        if key < 0 or key >= self.__size:
            raise QueueError('invalid key')
        cursor = self.__head
        for _ in range(key):
            cursor = cursor.next
        return cursor.data
    
    def __iter__(self):
        '''special method that adds a iterator to the stack'''
        cursor = self.__head
        while cursor:
            yield cursor.data
            cursor = cursor.next