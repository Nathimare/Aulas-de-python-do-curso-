#concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_concatenada = (lista1 + lista2)

print("lista1",lista1)
print("lista2",lista2)
print("Lista concatenada:",lista_concatenada)

lista_concatenada.insert(4, 100)
print("Lista concantenada após modificações", lista_concatenada)