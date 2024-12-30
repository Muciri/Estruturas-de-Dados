import numpy as np

class pilha_sequencial:
    #CONSTRUTOR
    def __init__(self, tamanho: int):
        self.__dados = np.full(tamanho, None)
        self.__topo = -1
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
    
        pilha = '|'
        for i in self.__dados[:self.__topo + 1]:
            pilha += f'{i}, '
        pilha = pilha.rstrip(', ') + '<|' 
        return pilha
    
    def __len__(self):
        return self.__topo + 1
    
    #MÉTODOS DE CONTROLE
    def cheia(self):
        return self.__topo == len(self.__dados)
    
    def vazia(self):
        return self.__topo == -1
    
    def topo(self):
        if not self.vazia():
            return self.__dados[self.__topo]  
        else:
            raise IndexError("a pilha está vazia")
    
    #MÉTODOS GERAIS
    def empilha(self, carga:any):
        if not self.cheia():
            self.__topo += 1
            self.__dados[self.__topo] = carga
        else:
            raise IndexError("a pilha está cheia")

    def desempilha(self):
        if not self.vazia():
            elemento = self.__dados[self.__topo]
            self.__dados[self.__topo] = None
            self.__topo -= 1
            return elemento
        else:
            raise IndexError("a pilha está vazia")
        
    def busca_elemento(self, num):
        if num < 0 or num > self.__topo:
            raise IndexError("valor fora do intervalo")
        return self.__dados[num]
    
    def busca_posicao(self, elemento):
        cont = -1
        for i in self.__dados:
            cont +=1
            if i == elemento:
                return cont
            if i == None:
                return -1