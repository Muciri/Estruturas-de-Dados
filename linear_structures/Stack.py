from Nodes.Node import Node

class StackError(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class Stack:
    '''
    Stack Data Structure \n
    ────────────────────────────────────────────────────────────────────────────────────── \n
    stacks are data structures that follow the Last In, First Out (LIFO)
    principle, meaning the last element added is the first one to be removed. \n
    This makes stacks useful in situations like undo features or backtracking algorithms. \n
    ────────────────────────────────────────────────────────────────────────────────────── \n
    author: Murilo Maciel Rodrigues \n
    Student of Systems for Internet - IFPB (Instituto Federal da Paraíba) 
    '''
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __str__(self):
        if self.empty():
            return '[]'
        
        string = '[>'
        cursor = self.__head
        while cursor != None:
            string += f'{str(cursor.data)}, '
            cursor = cursor.next
        string = string.rstrip(', ') + ']'

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
        '''returns the head of the stack'''
        return self.__head
    
    def empty(self):
        '''returns True if the stack is empty, otherwise returns False'''
        return self.__size == 0
    
    def pile(self, data:any):
        '''adds a new element to the stack'''
        new_element = Node(data)
        new_element.next = self.__head
        self.__head = new_element
        self.__size += 1
    
    def unpile(self):
        '''removes the head element to the stack if it is not empty and returns the element'''
        if self.empty():
            raise StackError('the stack is already empty')
        element = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return element
    
    def element(self, key:any):
        '''searchs an element from the Stack by its key. if the method can not find the element, it returns None'''
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
            raise StackError('invalid key')
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