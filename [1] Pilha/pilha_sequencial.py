import numpy as np

class PilhaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

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
        return self.__topo + 1 == len(self.__dados)
    
    def vazia(self):
        return self.__topo == -1
    
    def topo(self):
        if self.vazia():
            raise PilhaError("a pilha está vazia")
        return self.__dados[self.__topo]       
    
    #MÉTODOS GERAIS
    def empilha(self, carga:any):
        if self.cheia():
            raise PilhaError("a pilha está cheia")
        # self.__topo += 1
        self.__dados[self.__topo + 1] = carga
        self.__topo += 1
            

    def desempilha(self):
        if self.vazia():
            raise PilhaError("a pilha está vazia")
        elemento = self.__dados[self.__topo]
        self.__dados[self.__topo] = None
        self.__topo -= 1
        return elemento     
        
    def busca_elemento(self, num):
        if num < 0 or num > self.__topo:
            raise PilhaError("valor fora do intervalo")
        return self.__dados[num]
    
    def busca_posicao(self, elemento):
        cont = -1
        for i in self.__dados:
            cont +=1
            if i == elemento:
                return cont
            if i == None:
                return -1
            
#teste
if __name__ == '__main__':   
    teste = pilha_sequencial(10)

    teste.empilha('1')
    teste.empilha('2')
    teste.empilha('3')
    teste.empilha('4')
    teste.empilha('5')
    
    print(teste)
    teste.desempilha()
    teste.desempilha()
    print(teste)

    print(teste.busca_elemento(0))
    print(teste.busca_elemento(2))

    print(teste.busca_posicao('3'))
    print(teste.busca_posicao('4'))

    print(f'topo: {teste.topo()}')