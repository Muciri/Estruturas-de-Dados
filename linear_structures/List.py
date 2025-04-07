from Nodes.Node import Node

class ListError(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class List():
    '''
    List Data Structure \n
    ─────────────────────────────────────────────────────────────────────────────────────── \n
    lists are structures based in Python's built-in lists. In this structures, elements can be added, removed or modified in any position of the list \n
    lists are ideal for situations where you need efficient insertions and deletions and don't require random access to elements. \n
    ─────────────────────────────────────────────────────────────────────────────────────── \n
    author: Murilo Maciel Rodrigues \n
    Student of Systems for Internet - IFPB (Instituto Federal da Paraíba) 
    '''
    def __init__(self):
        self.__head = None
        self.__size = 0

    def __str__(self):
        if self.empty():
            return '[]'
        
        string = '['
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
        '''returns the head of the list'''
        return self.__head
    
    def empty(self):
        '''returns True if the list is empty, otherwise returns False'''
        return self.__size == 0
    
    def add(self, data:any, position:int):
        '''adds a new element to the list in a specific position'''
        new_element = Node(data)
        cursor = self.__head
        if position > self.__size:
            raise ListError('invalid position')
        if position == 0:
            self.__head = new_element
        else:
            for _ in range(position):
                previous = cursor
                cursor = cursor.next
            previous.next = new_element
            new_element.next = cursor
        self.__size += 1
    
    def append(self, data:any):
        '''adds a new element to the list in the last position'''
        self.add(data, self.__size)

    def pop(self, position:int):
        '''removes a element from the list in a specific position'''
        cursor = self.__head
        if position > self.__size:
            raise ListError('invalid position')
        if self.empty():
            raise ListError("the list is empty")
        
        if position == 0:
            self.__head = self.__head.next
        else:
            for _ in range(position):
                previous = cursor
                cursor = cursor.next
            previous.next = cursor.next
        self.__size -= 1
    
    def reverse(self):
        '''reverts the list'''
        for i in range(self.__size-1, -1, -1):
            self.append(self[i])
        for _ in range(int(self.__size/2)):
            self.pop(0)
    
    def element(self, key:any):
        '''searchs an element from the list by its key. if the method can not find the element, it returns None'''
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
            raise ListError('invalid key')
        cursor = self.__head
        for _ in range(key):
            cursor = cursor.next
        return cursor.data

    def __setitem__(self, key:int, data:any):
        '''special method to modify elements in the stack by their index'''
        if key < 0 or key >= self.__size:
            raise ListError('invalid key')
        cursor = self.__head
        for _ in range(key):
            cursor = cursor.next
        cursor.data = data
    
    def __iter__(self):
        '''special method that adds a iterator to the stack'''
        cursor = self.__head
        while cursor:
            yield cursor.data
            cursor = cursor.next