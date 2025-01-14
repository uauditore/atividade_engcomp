# Entrada do usuário
n = int(input("Digite um número inteiro N: "))

if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é: {fatorial}")
