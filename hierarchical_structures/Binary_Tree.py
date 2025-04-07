from Nodes.Tree_Node import Node

class TreeError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class BinaryTree:
    '''
    Simple Binary Tree Structure \n
    ─────────────────────────────────────────────────────────────── \n
    A binary tree is a data structure where each node has up to two children: a left child and a right child. \n
    It doesn't follow any specific order for storing values. \n
    ─────────────────────────────────────────────────────────────── \n
    author: Murilo Maciel Rodrigues \n
    Student of Systems for Internet - IFPB (Instituto Federal da Paraíba) 
    '''
    def __init__(self, data=None):
        self.size = 0
        if data is not None:
            self.root = Node(data)
            self.size = 1
        else:
            self.root = None
            self.size = 0
        self.cursor = self.root

    def __len__(self):
        return self.size

    def create_root(self, data):
        '''creates the root to the tree'''
        if self.root is not None:
            raise TreeError("root already exists")
        self.root = Node(data)
        self.cursor = self.root
        self.size = 1

    def empty(self):
        '''returns if the tree is empty'''
        return self.size == 0

    def get_root(self)->any:
        '''returns the tree's root'''
        return self.root
    
    def get_cursor(self):
        '''returns the tree's cursor'''
        return self.cursor.data
    
    def reset_cursor(self):
        '''resets the tree's cursor'''
        self.cursor = self.root
    
    def down_left(self):
        '''lower the cursor one level to the left'''
        if self.cursor is None or self.cursor.left is None:
            return
        self.cursor = self.cursor.left

    def down_right(self):
        '''lower the cursor one level to the right'''
        if self.cursor is None or self.cursor.right is None:
            return
        self.cursor = self.cursor.right

    def add_left(self, data):
        '''adds a left child to the cursor'''
        if self.root is None:
            raise TreeError("the tree is missing a root")
        else:
            if self.cursor is None:
                raise TreeError("cursor's node already has a left child")
            self.cursor.left = Node(data)
            self.size += 1
    
    def add_right(self, data):
        '''adds a right child to the cursor'''
        if self.root is None:
            raise TreeError("the tree is missing a root")
        else:
            if self.cursor is None:
                raise TreeError("cursor's node already has a right child")
            self.cursor.right = Node(data)
            self.size += 1

    def pos_order(self):
        '''prints tree's elements in pos_order'''
        self.__pos_order(self.root)

    def __pos_order(self, raiz):
        if raiz is not None:
            self.__pos_order(raiz.left)
            self.__pos_order(raiz.right)
            print(raiz.data, end=' ')
    
    def pre_order(self):
        '''prints tree's elements in pre_order'''
        self.__pre_order(self.root)

    def __pre_order(self, raiz):
        if raiz is not None:
            print(raiz.data, end=' ')
            self.__pre_order(raiz.left)
            self.__pre_order(raiz.right)
    
    def in_order(self):
        '''prints tree's elements in order'''
        self.__in_order(self.root)
    
    def __in_order(self, raiz):
        if raiz is not None:            
            self.__in_order(raiz.left)
            print(raiz.data, end=' ')
            self.__in_order(raiz.right)