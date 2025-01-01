from pilha_sequencial import pilha_sequencial
from pilha_encadeada import pilha_encadeada

#teste pilha sequencial
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

#teste pilha encadeada
teste = pilha_encadeada()

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
print(teste.busca('3'))

print(teste.busca_posicao('3'))
print(teste.busca_posicao('4'))

print(f'topo: {teste.topo()}')