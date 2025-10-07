#Abrir um arquivo em modo de leitura:
arquivo = open("arquivo.text", "r")

#Ler o conteúdo do arquivo:
conteudo = arquivo.read()

#Fechar o arquivo após a leitura:
arquivo.close()

#Imprimir o conteúdo lido:
print(conteudo)

#Abrir um arquivo em modo de escrita:
arquivo = open("novo_arquivo.txt", "w")

#Escrever no arquivo:
arquivo.white("Este é um novo arquivo criando por Python!")

#Fechar o arquivo após a escrita
arquivo.close()