from hierarchical_structures.Binary_Tree import BinaryTree

print('=-=-=-=-=-=-=-Simple Tree Tests=-=-=-=-=-=-=-')
arvore = BinaryTree(10)

print(arvore.get_cursor())
print(len(arvore))

arvore.add_right(6)
arvore.down_right()
print(arvore.get_cursor())
arvore.add_left(7)
arvore.add_right(8)
raiz = arvore.get_root()
print(arvore.get_cursor())
print(len(arvore))

arvore.down_right()
arvore.add_right(9)
print(arvore.get_root())
print(arvore.get_cursor())
print(len(arvore))

arvore.pre_order()
print()
arvore.in_order()
print()
arvore.pos_order()