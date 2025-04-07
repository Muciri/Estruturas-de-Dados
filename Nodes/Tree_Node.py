class Node:
    def __init__(self, data:any):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, new:any):
        self.__data = new

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, new:object):
        self.__left = new

    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, new:object):
        self.__right = new