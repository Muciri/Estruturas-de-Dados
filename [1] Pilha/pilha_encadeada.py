class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

class pilha_encadeada:
    #CONSTRUTOR
    def __init__(self):
        self.__head = None
        self.__topo = -1
    
    #MÉTODOS ESPECIAIS
    def __str__(self):
        if self.vazia():
            return '||'
        pilha = '|>'
        cursor = self.__head
        while(cursor != None):
            pilha += f'{cursor.carga}, '
            cursor = cursor.prox

        pilha = pilha.rstrip(', ') + '|' 
        return pilha
    
    def __len__(self):
        return self.__topo + 1
    
    #MÉTODOS DE CONTROLE
    def vazia(self):
        return self.__topo == -1
    
    def topo(self):
        if not self.vazia():
            return self.__head.carga   
        else:
            raise IndexError("a pilha está vazia")
    
    #MÉTODOS GERAIS
    def empilha(self, carga:any):
        self.__topo += 1
        novo = no(carga)
        novo.prox = self.__head
        self.__head = novo

    def desempilha(self):
        if not self.vazia():
            self.__topo -= 1
            elemento = self.__head.carga
            self.__head = self.__head.prox
            return elemento
        else:
            raise IndexError("a pilha está vazia")
        
    def busca(self, elemento):
        cursor = self.__head
        while (cursor != None):
            if cursor.carga == elemento:
                return cursor.carga
            cursor = cursor.prox
        raise IndexError(f'{elemento} não encontrado na pilha')
    
    def busca_elemento(self, num:int):
        if num < 0 or num > self.__topo:
            raise IndexError("valor fora do intervalo")
        cont = 0
        cursor = self.__head
        while cont != num:
            cursor = cursor.prox
            cont += 1
        return cursor.carga
    
    def busca_posicao(self, elemento):
        cont = 0
        cursor = self.__head
        while (cursor != None):
            if cursor.carga == elemento:
                return cont
            cursor = cursor.prox
            cont += 1
        return -1