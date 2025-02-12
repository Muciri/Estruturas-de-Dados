class arvoreError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class no:
    def __init__(self, carga):
        self.carga = carga
        self.esq = None
        self.dir = None 

class arvore_binaria_ordenada:
    def __init__(self, raiz=None):
        self.__raiz = no(raiz) if raiz != None else None
        self.__tamanho = 0 if raiz == None else 1

    #função STR copiada provisoriamente do copilot
    def __str__(self):
        return self._str_helper(self.__raiz)

    def _str_helper(self, node, level=0, prefix="Root: "):
        result = ""
        if node is not None:
            result += " " * (level * 4) + prefix + str(node.carga) + "\n"
            if node.esq is not None:
                result += self._str_helper(node.esq, level + 1, "L--- ")
            if node.dir is not None:
                result += self._str_helper(node.dir, level + 1, "R--- ")
        return result

    def __len__(self):
        return self.__tamanho
    
    def vazia(self):
        '''retorna se a árvore está vazia'''
        return self.__tamanho == 0
    
    def add_raiz(self, carga):
        '''adiciona um elemento à raiz, caso a árvore esteja vazia'''
        if not self.vazia():
            raise arvoreError('a árvore já tem raiz')
        self.__raiz = no(carga)
        self.__tamanho += 1

    def add(self, carga):
        '''adiciona um elemento à árvore'''
        self.__add_aux(self.__raiz, carga) 
        self.__tamanho += 1

    def __add_aux(self, raiz, carga):
        if raiz == None:
            return no(carga)
        elif carga < raiz.carga:
            raiz.esq = self.__add_aux(raiz.esq, carga)
        elif carga >= raiz.carga:
            raiz.dir = self.__add_aux(raiz.dir, carga)

        return raiz

    def busca(self, key):
        '''busca um elemento da árvore'''
        return self.__busca_aux(self.__raiz, key)

    def __busca_aux(self, raiz, key):
        if raiz == None:
            raise arvoreError('elemento não encontrado')
        elif key == raiz.carga:
            return raiz.carga
        elif key < raiz.carga:
            return self.__busca_aux(raiz.esq, key)
        elif key > raiz.carga:
            return self.__busca_aux(raiz.dir, key)
        
        return raiz.carga
    
    def conta_folhas(self):
        '''conta quantos nós folha a árvore tem'''
        return self.__conta_folhas_aux(self.__raiz)

    def __conta_folhas_aux(self, raiz):
        if raiz == None:
            return 0
        if raiz.esq == None and raiz.dir == None:
            return 1
        
        return self.__conta_folhas_aux(raiz.esq) + self.__conta_folhas_aux(raiz.dir)
    
    def preordem(self):
        self.__preordem(self.__raiz)
        print('')
    
    def __preordem(self, raiz):
        if raiz != None:
            print(raiz.carga, end=' ')
            self.__preordem(raiz.esq)
            self.__preordem(raiz.dir)
    
    def posordem(self):
        self.__posordem(self.__raiz)
        print('')

    def __posordem(self, raiz):
        if raiz != None:
            self.__preordem(raiz.esq)
            self.__preordem(raiz.dir)
            print(raiz.carga, end=' ')
    
    def emordem(self):
        self.__emordem(self.__raiz)
        print('')

    def __emordem(self, raiz):
        if raiz != None:
            self.__preordem(raiz.esq)
            print(raiz.carga, end=' ')
            self.__preordem(raiz.dir)

if __name__ == "__main__":
    arvore = arvore_binaria_ordenada(10)
    
    arvore.add(5)
    arvore.add(4)
    arvore.add(16)
    arvore.add(6)
    arvore.add(10)
    arvore.add(15)
    arvore.add(20)
    arvore.add(9)

    print(arvore)
    print('nós folha ',arvore.conta_folhas())
    print('busca por elemento: ',arvore.busca(15))
    print('tamanho da árvore ',len(arvore))

    print('\npré-ordem:')
    arvore.preordem()
    print('pós-ordem:')
    arvore.posordem()
    print('em-ordem:')
    arvore.emordem()