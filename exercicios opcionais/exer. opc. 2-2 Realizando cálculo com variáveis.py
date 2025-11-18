numero1 = 10
numero2 = 20

Soma = numero1 + numero2
Subtracao = numero2 - numero1

print("Soma: ",Soma)
print("Subtração :", Subtracao)

print("--------------------------------------------------------")

print("Coloque dois números onde serão usandos para os calculos")

N1 = int(input("Digite um número: "))
N2 = int(input("Digite o segundo número"))

while True:
    print("\nCalculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Parar")

    opcao = int(input("Agora escolha a forma de calculo:"))

    if opcao == 1:
        Som = N1 + N2
        print("Resultado: ",Som)
    elif opcao == 2:
        Sub = N1 - N2
        print("Resultado: ",Sub)
    elif opcao == 3:
        Mult = N1 * N2
        print("Resultado: ",Mult)
    elif opcao == 4:
        Div = N1 / N2
        print("Resultado: ",Div)
    elif opcao == 5:
        break
    else:
        print("Escolha uma opção válida")