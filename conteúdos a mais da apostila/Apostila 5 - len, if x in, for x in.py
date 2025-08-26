#Conteúdos extras apresentados na apóstila

#Lista do tipo "Int"
minha_lista = [1,5,6,7,9,11,30,33,40,44,55]

#Verifica a quantidade de elementos na lista:
tamanho_da_lista = len(minha_lista)
print(tamanho_da_lista, "números")

print("------------------------")

#Verifica se um elemento está presente na lista:
if 40 in minha_lista:
    print("40 está na lista")
else:
    print("40 não está na lista")

print("------------------------")

#Percorrer a lista usando "loops":
for elemento in minha_lista:
    print(elemento)