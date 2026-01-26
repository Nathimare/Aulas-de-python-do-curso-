#Desafio 05
#Fazer um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
n1 = int(input("Coloque um número: "))
a = n1 - 1
s = n1 + 1
print("Agora iremos mostrar o antecessor, o seu número e o sucessor: ", end="")
print(a,",",n1,",",s)

print("\n")

#Desafio 06
#Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num1 = int(input("Digite um número para o calculo: "))
do = num1 * 2
tri = num1 * 3
r = num1 ** (1/2) # também se usa 'pow' - pow(n, (1/2)
print("O dobro do seu número é: {}; O triplo do seu número é: {}; A raiz quadrada do seu número é: {:.2f}".format(do, tri, r))

print("\n")

#Desafio 07
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
no1 = float(input("Digite a primeira nota do aluno: "))
no2 = float(input("Digite a segunda nota do aluno: "))
print("A média do aluno é: {:.1f}".format((no1 + no2) / 2))

print("\n")

#Desafio 08
#Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = int(input("Digite um número em metros, que mostraremos esse mesmo número em centímertros e milímetros: "))
c = m * 100
mm = m * 1000
print("O seu número é: {}M, em centímetros fica {}CM e em milímetros fica {}MM".format(m, c, mm))

print("\n")

#Desafio 09
#Fazer um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
tab = int(input("Digite um número pra tabuada"))
print("="*15)
print("{} X {:2} = {}".format(tab, 1, tab*1))
print("{} X {:2} = {}".format(tab, 2, tab*2))
print("{} X {:2} = {}".format(tab, 3, tab*3))
print("{} X {:2} = {}".format(tab, 4, tab*4))
print("{} X {:2} = {}".format(tab, 5, tab*5))
print("{} X {:2} = {}".format(tab, 6, tab*6))
print("{} X {:2} = {}".format(tab, 7, tab*7))
print("{} X {:2} = {}".format(tab, 8, tab*8))
print("{} X {:2} = {}".format(tab, 9, tab*9))
print("{} X {:2} = {}".format(tab, 10, tab*10))
print("="*15)

print("\n")

#Desafio 010
#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1.00 = R$3.27
din = float(input("Diga quanto de dinheiro você tem? R$"))
dol = din / 3.27
print("Você pode trocar os seus {} reais por {:.2f} dólares".format(din, dol))

print("\n")

#Desafio 011
#fazer um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m².
la = float(input("Diga quanto de largura tem a sua parede: "))
al = float(input("Diga quanto de altura tem a sua parede: "))
ar = la * al
print("Sua parede tem {}M².".format(ar), end=" ")
print("Sua parede precisara de {:.2f} litros de tinta".format(ar/2))

print("\n")

#Desafio 012
#fazer um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
pr = float(input("Digite o preço do seu produto? R$"))
print("O seu produto de {} com 5% de desconto fica: R${:.2f}".format(pr, pr - pr * 0.05))

print("\n")

#Desafio 013
#Fazer um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
sa = float(input("Diga o seu salário: "))
print("Você teve um aumento de 15%! O seu salário de {} está atualmente de: {:.2f}".format(sa, sa + sa * 0.15))