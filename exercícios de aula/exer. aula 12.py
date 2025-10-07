#criando arquivo
arquivo = open('texto_salvo.txt', 'w')

#código para escrever no txt
def gravar_arquivo():
    with open('texto_salvo.txt', 'a') as arquivo:
        while True:
            linha = input("Digite uma linha de texto (ou 'fim' para sair): ")
            if linha.lower() == 'fim':
                break
            arquivo.write(linha + '\n')

def ler_arquivo():
    with open('texto_salvo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo \"texto_salvo.txt\":")
        print(conteudo)

gravar_arquivo()
ler_arquivo()

arquivo.close()