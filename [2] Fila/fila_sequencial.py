import numpy as np

class FilaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

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
    
        fila = '|>'
        cursor = self.__frente
        for _ in range(self.__tamanho):
            fila += f'{self.__dados[cursor]}, '
            cursor = (cursor + 1) % len(self.__dados)
        fila = fila.rstrip(', ') + '<|' 
        return fila
    
    def __len__(self):
        return self.__tamanho
    
    #MÉTODOS DE CONTROLE
    def cheia(self):
        return self.__tamanho == len(self.__dados)
    
    def vazia(self):
        return self.__tamanho == 0
    
    def frente(self):
        if not self.vazia():
            return self.__dados[self.__frente]  
        else:
            raise FilaError("a fila está vazia")
    
    #MÉTODOS GERAIS
    def enfileira(self, carga:any):
        if self.cheia():    
            raise FilaError("a fila está cheia")    
        self.__fim = (self.__fim + 1) % len(self.__dados)
        self.__dados[self.__fim] = carga
        self.__tamanho += 1

    def desenfileira(self):
        if self.vazia():
            raise FilaError("a fila está vazia")
        elemento = self.__dados[self.__frente]
        self.__dados[self.__frente] = None
        self.__frente = (self.__frente +1) % len(self.__dados)
        self.__tamanho -= 1
        return elemento 

    def busca(self, elemento):
        cursor = self.__frente
        for i in range(len(self)):
            if self.__dados[cursor] == elemento:
                return self.__dados[cursor]
            cursor = (cursor + 1) % len(self.__dados)   
        raise FilaError(f"Elemento {elemento} não encontrado na fila") 

    def busca_elemento(self, num):
        if num < 0 or num >= self.__tamanho:
            raise FilaError("valor fora do intervalo")
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

#teste
if __name__ == '__main__':   
    teste = fila_sequencial(10)

    teste.enfileira('1')
    teste.enfileira('2')
    teste.enfileira('3')
    teste.enfileira('4')
    teste.enfileira('5')

    print(teste)
    teste.desenfileira()
    teste.desenfileira()
    print(teste)

    print(teste.busca_elemento(0))
    print(teste.busca_elemento(1))
    print(teste.busca_elemento(2))

    print(teste.busca('3'))
    print(teste.busca('4'))

    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))