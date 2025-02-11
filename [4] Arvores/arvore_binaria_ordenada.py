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
        self.__tamanho = 0

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
    
    def __add_aux(self, raiz, carga):
        if raiz == None:
            return no(carga)
        if carga < raiz.carga:
            raiz.esq = self.__add_aux(raiz.esq, carga)
        elif carga >= raiz.carga:
            raiz.dir = self.__add_aux(raiz.dir, carga)
        
        self.__tamanho += 1
        return raiz

    def add(self, carga):
        self.__add_aux(self.__raiz, carga) 

    def busca(self, raiz, key):
        if raiz == key:
            return True
    
    def __conta_folhas_aux(self, raiz):
        if raiz == None:
            return 0
        if raiz.esq == None and raiz.dir == None:
            return 1
        if len(self) == 1:
            return 1 
        return self.__conta_folhas_aux(raiz.esq) + self.__conta_folhas_aux(raiz.dir)
    
    def conta_folhas(self):
        return self.__conta_folhas_aux(self.__raiz)
        

if __name__ == "__main__":
    arvore = arvore_binaria_ordenada(10)
    
    arvore.add(5)
    arvore.add(4)
    arvore.add(16)
    arvore.add(6)
    arvore.add(10)
    arvore.add(15)
    arvore.add(20)

    print(arvore)
    print(arvore.conta_folhas())
    