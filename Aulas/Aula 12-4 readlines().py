with open('novo_arquivo.txt', 'r') as arquivo:
    #ler as duas linhas e cria um espaço entre elas
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)