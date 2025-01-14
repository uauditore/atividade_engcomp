# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar os números do usuário
n1 = int(input("Informe o primeiro número (início do intervalo): "))
n2 = int(input("Informe o segundo número (fim do intervalo): "))

# Garantir que n1 seja menor ou igual a n2
if n1 > n2:
    n1, n2 = n2, n1

# Inicialização das variáveis
soma_pares = 0
soma_impares = 0
quantidade_primos = 0

# Laço de repetição no intervalo [n1, n2]
for numero in range(n1, n2 + 1):
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero
    if eh_primo(numero):
        quantidade_primos += 1

# Exibir os resultados
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
print(f"Quantidade de números primos: {quantidade_primos}")
