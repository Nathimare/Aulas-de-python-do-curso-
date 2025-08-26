print("Bem-vindo(a) à lista de compras!")
print("Digite o nome do item que deseja comprar (ou 'sair' para encerrar):")

lista_compras = []
item = input()

while item != "sair":
    lista_compras.append(item)
    item = input()

print("\nAqui está a sua lista de compras:")
for i, item in enumerate(lista_compras, start=1):
    print(f"{i}. {item}")