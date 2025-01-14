Início
    Escreva "Digite a altura de uma das faces triangulares da pirâmide (em metros):"
    Leia Altura_Face
    Escreva "Digite a base de uma das faces triangulares da pirâmide (em metros):"
    Leia Base_Face

    # Cálculo da área de uma face triangular
    Area_Face = 0.5 * Base_Face * Altura_Face

    # Cálculo da área total das faces triangulares (4 faces)
    Area_Faces_Triangulares = 4 * Area_Face

    # Cálculo da área da base quadrada
    Area_Base = Base_Face * Base_Face

    # Cálculo da área total a ser pintada
    Area_Total = Area_Faces_Triangulares + Area_Base

    # Cálculo do total de litros de tinta necessários (1 litro para 2 m²)
    Litros_Tinta = Area_Total / 2

    # Cálculo da quantidade de latas de tinta necessárias (arredondar para cima)
    Se Litros_Tinta mod 5 = 0 então
        Latas_Necessarias = Litros_Tinta / 5
    Caso contrário
        Latas_Necessarias = (Litros_Tinta div 5) + 1
    FimSe

    # Cálculo do custo total
    Custo_Total = Latas_Necessarias * 100

    # Exibir os resultados
    Escreva "Área total a ser pintada: ", Area_Total, " m²"
    Escreva "Quantidade de latas de tinta necessárias: ", Latas_Necessarias
    Escreva "Custo total: R$ ", Custo_Total
Fim
