numero_secreto = 42
tentativa = None
while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número secreto: "))
    if tentativa != numero_secreto:
        print("Tente novamente!")
print("Parabéns! você acertou o número secreto!")