import re

def encontrar_numeros(texto):
    padrao = r'\(\d{2}\) \d{4,5}-\d{4}'
    numeros_encontrados = re.findall(padrao, texto)
    return numeros_encontrados

texto = "Entre em contato pelos números (11) 9876-5432 ou (22) 34567-8901"
numeros = encontrar_numeros(texto)
print(numeros)