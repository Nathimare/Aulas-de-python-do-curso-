import csv

def adicionar_despesa(despesas, valor, categoria):
    despesas.append((valor, categoria))
    print("Despesa de R$ {:.2f} na categoria '{}' adicionada com sucesso!".format(valor, categoria))

def adicionar_receita(receitas, valor, categoria):
    receitas.append((valor, categoria))
    print("Receita de R$ {:.2f} na categoria '{}' adicionada com sucesso!".format(valor, categoria))

def calcular_saldo(despesas, receitas):
    total_despesas = sum([valor for valor, _ in despesas])
    total_receitas = sum([valor for valor, _ in receitas])
    return total_receitas - total_despesas

def mostrar_saldo(despesas, receitas):
    saldo = calcular_saldo(despesas, receitas)
    print("\nSaldo atual: R$ {:.2f}\n".format(saldo))

def gerar_relatorio(despesas, receitas):
    print("\nRelatório de Despesas por categoria:")
    categorias_despesas = {}
    for valor, categoria in despesas:
        categorias_despesas[categoria] = categorias_despesas.get(categoria, 0) + valor

    for categoria, valor_total in categorias_despesas.items():
        print("- {} : R$ {:.2f}".format(categoria, valor_total))

    print("\nRelatório de Receitas por Categoria:")
    categorias_receitas = {}
    for valor, categoria in receitas:
        categorias_receitas[categoria] = categorias_receitas.get(categoria, 0) + valor

    for categoria, valor_total in categorias_receitas.items():
        print("- {} : R$ {:.2f}".format(categoria, valor_total))

def exportar_dados(despesas, receitas):
    with open('controle_financeiro.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["Categoria", "Despesa", "Receita"])

        for valor, categoria in despesas:
            writer.writerow([categoria, valor, ""])

        for valor, categoria in receitas:
            writer.writerow([categoria, "", valor])

    print("\nDados exportados para 'controle_financeiro.csv' com sucesso!")

def main():
    despesas = []
    receitas = []

    while True:
        print("\nControle Financeiro\n")
        print("1 - Adicionar despesa")
        print("2 - Adicionar receita")
        print("3 - Ver saldo atual")
        print("4 - Gerar relatórios")
        print("5 - Exportar dados para CSV")
        print("6 - Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor da despesa: R$ "))
            categoria = input("Digite a categoria da despesa: ")
            adicionar_despesa(despesas, valor, categoria)
        elif opcao == 2:
            valor = float(input("Digite o valor da receita: R$ "))
            categoria = input("Digite a categoria da receita: ")
            adicionar_receita(receitas, valor, categoria)
        elif opcao == 3:
            mostrar_saldo(despesas, receitas)
        elif opcao == 4:
            gerar_relatorio(despesas, receitas)
        elif opcao == 5:
            exportar_dados(despesas, receitas)
        elif opcao == 6:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()