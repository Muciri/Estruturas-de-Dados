from pilha_encadeada import pilha_encadeada

class No:
    def __init__(self, carga):
        self.esq = self.dir = None
        self.carga = carga
    
    def __str__(self):
        return str(self.carga)

class ArvoreBinaria:
    def __init__(self, carga=None):
        self.tamanho = 0
        if carga is not None:
            self.raiz = No(carga)
            self.tamanho = 1
        else:
            self.raiz = None
            self.tamanho = 0
        self.cursor = self.raiz
        self.pilha = pilha_encadeada()

    def criar_raiz(self, carga):
        if self.raiz is not None:
            raise Exception("Raiz já existe")
        self.raiz = No(carga)
        self.cursor = self.raiz
        self.tamanho = 1

    def esta_vazia(self):
        return self.tamanho == 0

    def get_raiz(self)->any:
        return self.raiz
    
    def get_cursor(self):
        return self.cursor.carga
    
    def reset_cursor(self):
        self.cursor = self.raiz
    
    def desce_esquerda(self):
        if self.cursor is None or self.cursor.esq is None:
            return
        self.pilha.empilha(self.cursor)
        self.cursor = self.cursor.esq

    def desce_direita(self):
        if self.cursor is None or self.cursor.dir is None:
            return
        self.pilha.empilha(self.cursor)
        self.cursor = self.cursor.dir
    
    def back(self):
        self.cursor = self.pilha.topo()

    def add_esq(self, carga):
        if self.raiz is None:
            raise Exception("Arvore sem raiz")
        else:
            if self.cursor is None:
                raise Exception("nó do cursor já tem um filho esquerdo")
            self.cursor.esq = No(carga)
            self.tamanho += 1
    
    def add_dir(self, carga):
        if self.raiz is None:
            raise Exception("Arvore sem raiz")
        else:
            if self.cursor is None:
                raise Exception("nó do cursor já tem um filho esquerdo")
            self.cursor.dir = No(carga)
            self.tamanho += 1
    
    def esvaziar(self):
        self.raiz = None
        for _ in range(len(self.pilha)):
            self.pilha.desempilha

    def pos_ordem(self):
        self.__pos_ordem(self.raiz)

    def __pos_ordem(self, raiz):
        if raiz is not None:
            self.__pos_ordem(raiz.esq)
            self.__pos_ordem(raiz.dir)
            print(raiz.carga, end=' ')
    
    def pre_ordem(self):
        self.__pre_ordem(self.raiz)

    def __pre_ordem(self, raiz):
        if raiz is not None:
            print(raiz.carga, end=' ')
            self.__pre_ordem(raiz.esq)
            self.__pre_ordem(raiz.dir)
    
    def em_ordem(self):
        self.__em_ordem(self.raiz)
    
    def __em_ordem(self, raiz):
        if raiz is not None:            
            self.__em_ordem(raiz.esq)
            print(raiz.carga, end=' ')
            self.__em_ordem(raiz.dir)
    
    def __len__(self):
        return self.tamanho

if __name__ == "__main__":
    arvore = ArvoreBinaria(10)

    print(arvore.get_cursor())
    print(len(arvore))

    arvore.add_dir(6)
    arvore.desce_direita()
    print(arvore.get_cursor())
    arvore.add_esq(7)
    arvore.add_dir(8)
    raiz = arvore.get_raiz()
    print(arvore.get_cursor())
    print(len(arvore))

    arvore.desce_direita()
    arvore.add_dir(9)
    print(arvore.get_raiz())
    print(arvore.get_cursor())
    print(len(arvore))

    arvore.pre_ordem()
    print()
    arvore.em_ordem()
    print()
    arvore.pos_ordem()

    arvore.esvaziar()
    print('\nárvore esvaziada')