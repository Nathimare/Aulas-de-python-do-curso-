print("="*20)
nome = "Gabriel"
print("Prazer em te conhecer {:20}!".format(nome))#Escrever o nome com 20 linhas alinhado na esquerda
print("Prazer em te conhecer {:>20}!".format(nome))#Escrever o nome com 20 linhas alinhado na direita
print("Prazer em te conhecer {:^20}!".format(nome))#Escrever o nome com 20 linhas centralizado
print("Prazer em te conhecer {:=^20}!".format(nome))#Escrever o nome com 20 linhas centralizado, colocando '=' em volta

print("\n")

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma vale {}".format(n1+n2), end=", ") #"End" junta o final
print("A mult é {}, o produto é {:.3f}".format(m, d), end=", ")
print("A divisão inteira é {}, e a potência é {}".format(di, e))