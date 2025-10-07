#criando um arquivo:
arquivo = open('novo_arquivo1.txt', 'w')

#código para escrever um texto no arquivo criado:
with open('novo_arquivo1.txt', 'w') as arquivo:
    arquivo.write('Este é um novo arquivo criado em Python.\n')
    arquivo.write('Aqui escrevemos mais uma linha de texto.\n')

#código para abrir o texto criado no console:
with open('novo_arquivo1.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
for linha in linhas:
    print(linha)

arquivo.close()