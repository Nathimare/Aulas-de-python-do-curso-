frase = input("Digite uma palavra: ")
vogais = "aeiou"
contador = 0
for caractere in frase.lower():
    if caractere in vogais:
        contador += 1

print("Número de vogais na frase: ", contador)