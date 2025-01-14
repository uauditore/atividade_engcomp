Início
    Parafuso_Preco = 0.70
    Porca_Preco = 0.25
    Arruela_Preco = 0.15
    
    Escreva "Digite a quantidade de parafusos:"
    Leia Quantidade_Parafuso
    Escreva "Digite a quantidade de porcas:"
    Leia Quantidade_Porca
    Escreva "Digite a quantidade de arruelas:"
    Leia Quantidade_Arruela
    Escreva "Digite a condição de pagamento (Dinheiro/Outro):"
    Leia Condicao_Pagamento

    # Cálculo dos valores com descontos individuais
    Valor_Parafuso = Quantidade_Parafuso × Parafuso_Preco × 0.80
    Valor_Porca = Quantidade_Porca × Porca_Preco × 0.90
    Valor_Arruela = Quantidade_Arruela × Arruela_Preco × 0.70

    Valor_Total_Itens = Valor_Parafuso + Valor_Porca + Valor_Arruela
    Quantidade_Total = Quantidade_Parafuso + Quantidade_Porca + Quantidade_Arruela

    # Verificar desconto adicional
    Se Quantidade_Total > 100 E Condicao_Pagamento = "Dinheiro" então
        Desconto_Adicional = Valor_Total_Itens × 0.11  
    Caso contrário
        Desconto_Adicional = 0
    FimSe

    Valor_Total_Descontos = (Quantidade_Parafuso × Parafuso_Preco × 0.20) +
                            (Quantidade_Porca × Porca_Preco × 0.10) +
                            (Quantidade_Arruela × Arruela_Preco × 0.30) +
                            Desconto_Adicional

    Valor_Total_Final = Valor_Total_Itens - Desconto_Adicional

    Escreva "Total de descontos: R$", Valor_Total_Descontos
    Escreva "Total a pagar: R$", Valor_Total_Final
Fim
