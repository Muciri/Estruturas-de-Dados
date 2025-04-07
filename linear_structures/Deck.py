from Nodes.Node import Node

class DeckError(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class Deck:
    '''
    Deck Data Structure \n
    ─────────────────────────────────────────────────────────────── \n
    Decks are more flexible structures that allow insertion and removal from both the front and the back. \n
    Decks are useful when you need both stack and queue behaviors in one structure. \n
    ─────────────────────────────────────────────────────────────── \n
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
        '''returns the head of the Deck'''
        return self.__head
    
    def tail(self):
        '''returns the tail of the Deck'''
        return self.__tail
    
    def empty(self):
        '''returns True if the Deck is empty, otherwise returns False'''
        return self.__size == 0
    
    def add_head(self, data:any):
        '''adds a new element to the Deck'''
        new_element = Node(data)
        new_element.next = self.__head
        self.__head = new_element
        self.__size += 1

    def add_tail(self, data:any):
        '''adds a new element to the Deck'''
        new_element = Node(data)
        if self.empty():
            self.__head = self.__tail = new_element
        else:
            self.__tail.next = new_element
            self.__tail = new_element
        self.__size += 1

    def pop_head(self):
        '''removes the head element to the Deck if it is not empty and returns the element'''
        if self.empty():
            raise DeckError('the stack is already empty')
        element = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return element

    def pop_tail(self):
        '''removes the head element to the queue if it is not empty and returns the element'''
        if self.empty():
            raise DeckError('the queue is already empty')
        element = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return element
    
    def reverse(self):
        '''reverts the Deck'''
        for i in range(self.__size-1, -1, -1):
            self.add_tail(self[i])
        for _ in range(int(self.__size/2)):
            self.pop_head()
    
    def element(self, key:any):
        '''searchs an element from the Deck by its key. if the method can not find the element, it returns None'''
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
            raise DeckError('invalid key')
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