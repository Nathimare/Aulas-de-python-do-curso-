#Desafio 01
#criar um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
print("===== DESAFIO 01 =====")
nome = input("Digite o seu nome:")
print(f"Óla {nome} ! Prazer em te conhecer!")

print("\n")

#Desafio 02
#criar um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
print("===== DESAFIO 02 =====")
dia = int(input("Digite o dia do seu nascimento: "))
mes = input("Digite o mês do seu nascimento: ")
ano = int(input("Digite o ano do seu nascimento"))
print(f"Você nasceu em {dia} de {mes} de {ano}. Correto?")

print("\n")

#Desafio 03
#Criar um script que leia dois números e tente mostrar a doma entre eles
print("===== DESAFIO 03 =====")
N1 = int(input("Primeiro número: "))
N2 = int(input("Segundo número: "))
soma = N1 + N2
print("A soma dos números dá:", soma)