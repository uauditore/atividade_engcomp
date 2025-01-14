def calculadora():
    def get_user_input(prompt, valid_options=None):
        while True:
            try:
                user_input = input(prompt)
                if valid_options and user_input not in valid_options:
                    print("Opção inválida! Tente novamente.")
                    continue
                return user_input
            except (EOFError):
                print("Erro ao receber entrada. Verifique o ambiente de execução ou defina valores fixos para teste.")
                return None

    while True:
        print("\nEscolha a operação desejada:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = get_user_input("Digite o número da operação desejada: ", valid_options=['1', '2', '3', '4', '5'])

        if opcao == '5':
            print("Encerrando o programa. Até mais!")
            break

        if opcao is None:
            print("Não foi possível receber a entrada. Encerrando o programa.")
            break

        try:
            num1 = int(get_user_input("Digite o primeiro número: "))
            num2 = int(get_user_input("Digite o segundo número: "))
        except (ValueError, TypeError):
            print("Por favor, insira números válidos.")
            continue

        if opcao == '1':
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")

        repetir = get_user_input("\nDeseja realizar outro cálculo? (s/n): ", valid_options=['s', 'n'])
        if repetir != 's':
            print("Encerrando o programa. Até mais!")
            break
        
if __name__ == "__main__":
    calculadora()