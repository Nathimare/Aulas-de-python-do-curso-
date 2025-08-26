#remover elementos iguais

numeros = [2, 4, 6, 8, 2, 10, 12, 14, 8]
print("Lista original:", numeros)

numeros_sem_repeticao = []

for n in numeros:
    if n not in numeros_sem_repeticao:
        numeros_sem_repeticao.append(n)
print("Lista sem repetição:", numeros_sem_repeticao)