# Código IF e ELSE
limite_passageiros = 5

# esse código faz eu colocar a quantidade de passageiros
num_passageiros = int(input("Digite o número de passageiros: "))

# esse código vai comparra se o Npassageiros é menor que o Lpassageiros
if num_passageiros <= limite_passageiros:
    print("O limite não foi excedido. Tenha uma boa viagem")
else:
    print("O limite de passageiros foi excedido, não é possível continuar")