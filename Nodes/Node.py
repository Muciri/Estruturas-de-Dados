class Node:
    def __init__(self, data:any):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, new:any):
        self.__data = new

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new:object):
        self.__next = new