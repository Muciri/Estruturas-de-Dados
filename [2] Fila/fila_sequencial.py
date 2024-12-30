import numpy as np

class fila_sequencial:
    #CONSTRUTOR
    def __init__(self, tamanho: int):
        self.__dados = np.full(tamanho, None)
        self.__frente = 0
        self.__fim = -1
        self.__tamanho = 0
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
    
        pilha = '|>'
        for i in self.__dados[:self.__tamanho]:
            if i != None:
                pilha += f'{i}, '
        pilha = pilha.rstrip(', ') + '<|' 
        return pilha
    
    def __len__(self):
        return self.__tamanho
    
    #MÉTODOS DE CONTROLE
    def cheia(self):
        return self.__tamanho == len(self.__dados)
    
    def vazia(self):
        return self.__tamanho == -1
    
    def frente(self):
        if not self.vazia():
            return self.__dados[self.__frente]  
        else:
            raise IndexError("a pilha está vazia")
    
    #MÉTODOS GERAIS
    def enfileira(self, carga:any):
        if self.cheia():    
            raise IndexError("a pilha está cheia")    
        self.__fim = (self.__fim + 1) % len(self.__dados)
        self.__dados[self.__fim] = carga
        self.__tamanho += 1

    def desenfileira(self):
        if self.vazia():
            raise IndexError("a pilha está vazia")
        elemento = self.__dados[self.__frente]
        self.__dados[self.__frente] = None
        self.__frente = (self.__frente +1) % len(self.__dados)
        return elemento 
        
    def busca_elemento(self, num):
        if num < 0 or num > self.__tamanho:
            raise IndexError("valor fora do intervalo")
        cursor = self.__frente
        for i in range(num):
            cursor = (cursor +1) % len(self.__dados)
        return self.__dados[cursor]
    
    def busca_posicao(self, elemento):
        cont = -1
        for i in self.__dados:
            if i != None:
                cont +=1
                if i == elemento:
                    return cont
        return -1