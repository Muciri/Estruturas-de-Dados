from fila_sequencial import fila_sequencial
from fila_encadeada import fila_encadeada

#teste fila encadeada
teste = fila_encadeada()
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
# print(f'topo: {teste.topo()}')

print('-----------------------------')

#teste fila sequencial
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