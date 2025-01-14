# Solicita o número de alunos da turma
num_alunos = int(input("Informe o número de alunos na turma: "))

# Itera para cada aluno e coleta as informações
for i in range(1, num_alunos + 1):
    print(f"\nAluno {i}:")
    
    # Lê o nome do aluno
    nome = input("Primeiro nome do aluno: ").strip()
    
    # Lê as notas das avaliações
    nota1 = float(input("Nota da primeira avaliação: "))
    nota2 = float(input("Nota da segunda avaliação: "))
    
    # Calcula a média
    media = (nota1 + nota2) / 2
    
    # Determina se o aluno foi aprovado ou reprovado
    status = "Aprovado" if media >= 7 else "Reprovado"
    
    # Exibe o resultado para o aluno
    print(f"{nome}: Média = {media:.2f} - {status}")

print("\nProcessamento concluído.")
