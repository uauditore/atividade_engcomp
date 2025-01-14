# Tabelas de opções
pratos = {
    1: ("Vegetariano", 180, 8.50),
    2: ("Peixe", 230, 12.30),
    3: ("Frango", 250, 7.50),
    4: ("Carne", 350, 10.50)
}

sobremesas = {
    1: ("Abacaxi", 75, 1.50),
    2: ("Sorvete Diet", 110, 3.50),
    3: ("Mousse Diet", 170, 3.00),
    4: ("Mousse Chocolate", 200, 2.50)
}

bebidas = {
    1: ("Chá", 20, 1.00),
    2: ("Suco de Laranja", 70, 2.50),
    3: ("Suco de Melão", 100, 3.00),
    4: ("Refrigerante Diet", 65, 2.00)
}

def exibir_menu(opcoes, categoria):
    print(f"\nEscolha uma opção de {categoria}:")
    for chave, (nome, calorias, preco) in opcoes.items():
        print(f"{chave}. {nome} - {calorias}kcal - R${preco:.2f}")
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: "))
            if escolha in opcoes:
                return opcoes[escolha]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        print("\nMontando a refeição:")
        
        # Escolha do prato
        prato = exibir_menu(pratos, "prato")
        
        # Escolha da sobremesa
        sobremesa = exibir_menu(sobremesas, "sobremesa")
        
        # Escolha da bebida
        bebida = exibir_menu(bebidas, "bebida")
        
        # Cálculo do total
        calorias_totais = prato[1] + sobremesa[1] + bebida[1]
        preco_total = prato[2] + sobremesa[2] + bebida[2]
        
        # Exibição dos resultados
        print("\nResumo da refeição:")
        print(f"Prato: {prato[0]} - {prato[1]}kcal - R${prato[2]:.2f}")
        print(f"Sobremesa: {sobremesa[0]} - {sobremesa[1]}kcal - R${sobremesa[2]:.2f}")
        print(f"Bebida: {bebida[0]} - {bebida[1]}kcal - R${bebida[2]:.2f}")
        print(f"Total de calorias: {calorias_totais}kcal")
        print(f"Preço total: R${preco_total:.2f}")
        
        # Perguntar se deseja continuar
        continuar = input("\nDeseja atender outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

# Executa o programa
main()
