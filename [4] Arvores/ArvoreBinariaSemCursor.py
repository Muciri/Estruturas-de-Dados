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
        # self.cursor = self.raiz

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

    def get(self, chave:any)->any:
        return self.__get(chave, self.raiz)

    def __get(self, chave:any, node:No)->No:
        if (node == None):
            return None # Nao encontrou a chave
        if ( chave == node.carga):
            return node
        
        noRetornado = self.__get( chave, node.esq)
        
        if (noRetornado):
            return noRetornado
        else:
            return self.__get( chave, node.dir)

    def add_esq(self, chave, carga):
        self.get(chave).esq = No(carga)
    
    def add_dir(self, chave, carga):
        self.get(chave).dir = No(carga)

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

    arvore.add_dir(10, 5)
    arvore.add_esq(10, 4)

    arvore.add_dir(5, '6')
    arvore.add_esq(4, [3])

    raiz = arvore.get_raiz()
    print('raiz: ',raiz)




    print(len(arvore))

    arvore.pre_ordem()
    print()
    arvore.em_ordem()
    print()
    arvore.pos_ordem()
    print('\ntamanho da árvore: ',len(arvore))