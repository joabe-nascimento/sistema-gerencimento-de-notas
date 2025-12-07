# =============================================================================
# Sistema de Gerenciamento de Notas de Alunos
# =============================================================================
# Este programa demonstra o uso de:
# - Dicionários (para armazenar dados dos alunos)
# - Listas (para armazenar as notas)
# - Loops (for e while)
# - Estruturas condicionais (if, elif, else)
# - Funções de entrada/saída (input, print)
# - Operadores aritméticos e de comparação
# =============================================================================

# -----------------------------------------------------------------------------
# PASSO 1: INICIALIZAÇÃO
# -----------------------------------------------------------------------------
# Criando um dicionário vazio para armazenar os dados dos alunos
# Estrutura: {nome_aluno: [nota1, nota2]}
dados_alunos = {}

# Solicitando ao usuário a quantidade de alunos a serem cadastrados
print("=" * 50)
print("   SISTEMA DE GERENCIAMENTO DE NOTAS DE ALUNOS")
print("=" * 50)
print()

# Usando int(input()) para garantir que o valor seja um inteiro
n = int(input("Quantos alunos serão cadastrados? "))
print()

# -----------------------------------------------------------------------------
# PASSO 2: LEITURA DOS DADOS (Loop for)
# -----------------------------------------------------------------------------
# Utilizando um laço for para iterar N vezes e coletar os dados
for i in range(n):
    print(f"--- Cadastro do Aluno {i + 1} ---")
    
    # Lendo o nome do aluno
    nome = input("Nome do Aluno: ")
    
    # Lendo as notas e convertendo para float (permite valores fracionários)
    nota1 = float(input("Nota 1 (N1): "))
    nota2 = float(input("Nota 2 (N2): "))
    
    # Armazenando no dicionário: chave = nome, valor = lista com as notas
    dados_alunos[nome] = [nota1, nota2]
    
    print()  # Linha em branco para melhor visualização

# -----------------------------------------------------------------------------
# PASSO 3: PROCESSAMENTO E EXIBIÇÃO (Loop for sobre o Dicionário)
# -----------------------------------------------------------------------------
print("=" * 60)
print("                    RELATÓRIO DE NOTAS")
print("=" * 60)
print()

# Percorrendo o dicionário usando o método .items()
# Isso permite acessar a chave (nome) e o valor (notas) simultaneamente
for nome, notas in dados_alunos.items():
    # Extraindo as notas da lista
    nota1 = notas[0]
    nota2 = notas[1]
    
    # CÁLCULO: Calculando a média simples
    media = (nota1 + nota2) / 2
    
    # CONDICIONAL: Determinando a situação do aluno
    # Usando estrutura if-elif-else com base nas regras fornecidas
    if media >= 60:
        situacao = "Aprovado"
    elif media < 30:
        situacao = "Reprovado"
    else:  # média >= 30 e média < 60
        situacao = "Sub"
    
    # SAÍDA: Imprimindo os resultados formatados
    print(f"Aluno: {nome}")
    print(f"  Notas: N1 = {nota1:.1f} | N2 = {nota2:.1f}")
    print(f"  Média: {media:.2f}")
    print(f"  Situação: {situacao}")
    print("-" * 40)

# -----------------------------------------------------------------------------
# RESUMO ESTATÍSTICO (Extra)
# -----------------------------------------------------------------------------
print()
print("=" * 60)
print("                  RESUMO DA TURMA")
print("=" * 60)

# Contadores para cada situação
aprovados = 0
reprovados = 0
sub = 0

# Usando outro loop for para contar as situações
for nome, notas in dados_alunos.items():
    media = (notas[0] + notas[1]) / 2
    
    if media >= 60:
        aprovados += 1
    elif media < 30:
        reprovados += 1
    else:
        sub += 1

print(f"Total de Alunos: {n}")
print(f"Aprovados: {aprovados}")
print(f"Em Sub: {sub}")
print(f"Reprovados: {reprovados}")
print("=" * 60)

print("\nPrograma finalizado com sucesso!")

