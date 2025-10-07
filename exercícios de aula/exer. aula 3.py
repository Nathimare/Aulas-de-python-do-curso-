idade = int(input("Digite a idade do visitante: "))
if idade < 4:
    print("Desculpe, crianças com menos de 4 anos não podem entrar no parque.")
elif idade <= 12:
    print("Acompanhado por um adulto, você pode entrar no parque de diversões!")
else:
    print("Você pode entrar no parque de diversões!")