while True:
    print("\n--- Calculadora ---")
    print("1 - Soma")
    print("2 - Multiplicação")
    print("3 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da calculadora... 👋")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print(f"Resultado: {n1 + n2}")
    elif opcao == "2":
        print(f"Resultado: {n1 * n2}")
    elif opcao == "3":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Opção inválida! Tente novamente.")