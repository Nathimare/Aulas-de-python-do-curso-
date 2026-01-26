# Dados dois números inteiros, escreva um programa em Python que retorne o produto deles somente se o resultado for igual ou menor que 1000.
# Caso contrário, retorne a soma.
# números
N1 = int(input("Digite o primeiro número:"))
N2 = int(input("Agora digite o segundo número:"))

resultado = N1 * N2

# Código
if resultado <= 1000:
    print("O resultado é",resultado)

else:
    resultado = N1 + N2
    print("O resultado é",resultado)

# Como era pra ser feito:

def multiplicar_ou_somar(num1,num2):
    produto = num1 * num2
    if produto <= 1000:
        return produto
    else:
        return num1 + num2
resultado = multiplicar_ou_somar(20,30)
print("O resultado é",resultado)

resultado = multiplicar_ou_somar(40,30)
print("O resultado é",resultado)