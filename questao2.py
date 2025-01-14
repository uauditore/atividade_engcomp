while True:
    try:
        valor1 = float(input("Informe o primeiro valor: "))
        while True:
            valor2 = float(input("Informe o segundo valor: "))
            if valor2 != 0:
                break
            print("O segundo valor não pode ser zero. Tente novamente.")
        resultado = valor1 / valor2
        print(f"Resultado da divisão: {resultado:.2f}")
        
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa finalizado.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
