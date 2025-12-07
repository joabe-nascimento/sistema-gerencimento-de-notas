# 📚 Sistema de Gerenciamento de Notas de Alunos

**Disciplina:** Programação em Python  
**Tema:** Algoritmos, Fluxogramas, Variáveis, Operadores, Estruturas de Controle e Estruturas de Dados (Listas, Tuplas, Dicionários)

---

## 1. Objetivo

O objetivo desta atividade é desenvolver um sistema de gerenciamento de notas para uma turma de alunos, aplicando os seguintes conceitos:

- Dicionários
- Listas
- Loops (while e for)
- Estruturas condicionais (if, elif, else)
- Funções de entrada/saída (input, print)
- Operadores aritméticos e de comparação

---

## 2. Descrição do Problema

O programa deve realizar as seguintes operações:

### 2.1 Leitura e Armazenamento dos Dados
- Ler o nome de N alunos e suas respectivas notas
- Armazenar em um dicionário onde:
  - **Chave:** nome do aluno (string)
  - **Valor:** lista contendo as notas [N1, N2]

### 2.2 Cálculo da Média
- Calcular a média final de cada aluno usando a fórmula:
  - `Média = (N1 + N2) / 2`

### 2.3 Determinação da Situação
| Situação | Condição |
|----------|----------|
| Aprovado | Média >= 60 |
| Sub | Média >= 30 e Média < 60 |
| Reprovado | Média < 30 |

### 2.4 Exibição dos Resultados
- Imprimir nome, notas, média e situação de cada aluno

---

## 3. Fluxograma

```
                              ┌─────────┐
                              │  INÍCIO │
                              └────┬────┘
                                   │
                                   ▼
                      ┌────────────────────────┐
                      │ dados_alunos = {}      │
                      │ (dicionário vazio)     │
                      └───────────┬────────────┘
                                  │
                                  ▼
                      ┌────────────────────────┐
                      │ Ler quantidade de      │
                      │ alunos (N)             │
                      └───────────┬────────────┘
                                  │
                                  ▼
                         ┌───────────────┐
                         │ i = 0         │
                         └───────┬───────┘
                                 │
                    ┌────────────▼────────────┐
                    │       i < N ?           │◄────────────┐
                    └────────────┬────────────┘             │
                          │              │                  │
                         SIM            NÃO                 │
                          │              │                  │
                          ▼              ▼                  │
          ┌───────────────────────┐   (Vai para            │
          │ Ler nome, N1, N2      │   exibição)            │
          └───────────┬───────────┘                        │
                      │                                    │
                      ▼                                    │
          ┌───────────────────────┐                        │
          │ dados_alunos[nome] =  │                        │
          │      [N1, N2]         │                        │
          └───────────┬───────────┘                        │
                      │                                    │
                      ▼                                    │
               ┌─────────────┐                             │
               │  i = i + 1  │─────────────────────────────┘
               └─────────────┘

                    ┌────────────────────────────────┐
                    │ Para cada (nome, notas) em     │◄────┐
                    │ dados_alunos.items():          │     │
                    └───────────────┬────────────────┘     │
                                    │                      │
                                    ▼                      │
                    ┌────────────────────────────────┐     │
                    │ media = (notas[0]+notas[1])/2  │     │
                    └───────────────┬────────────────┘     │
                                    │                      │
                         ┌──────────▼──────────┐           │
                         │   media >= 60 ?     │           │
                         └──────────┬──────────┘           │
                              │           │                │
                            SIM          NÃO               │
                              │           │                │
                              ▼           ▼                │
                    ┌──────────────┐  ┌──────────────┐     │
                    │  situacao =  │  │ media < 30 ? │     │
                    │  "Aprovado"  │  └──────┬───────┘     │
                    └──────┬───────┘    │         │        │
                           │          SIM        NÃO       │
                           │           │          │        │
                           │           ▼          ▼        │
                           │  ┌────────────┐ ┌─────────┐   │
                           │  │ situacao = │ │situacao │   │
                           │  │"Reprovado" │ │ ="Sub"  │   │
                           │  └─────┬──────┘ └────┬────┘   │
                           │        │             │        │
                           └────────┴──────┬──────┘        │
                                           │               │
                                           ▼               │
                           ┌───────────────────────────┐   │
                           │ Imprimir: nome, notas,    │   │
                           │ media, situacao           │   │
                           └─────────────┬─────────────┘   │
                                         │                 │
                                         └─────────────────┘
                                         (próximo aluno)
                                               │
                                               ▼
                                         ┌──────────┐
                                         │   FIM    │
                                         └──────────┘
```

---

## 4. Código Fonte em Python

```python
# =============================================================================
# Sistema de Gerenciamento de Notas de Alunos
# =============================================================================

# -----------------------------------------------------------------------------
# PASSO 1: INICIALIZAÇÃO
# -----------------------------------------------------------------------------
# Criando um dicionário vazio para armazenar os dados dos alunos
dados_alunos = {}

# Solicitando ao usuário a quantidade de alunos a serem cadastrados
print("=" * 50)
print("   SISTEMA DE GERENCIAMENTO DE NOTAS DE ALUNOS")
print("=" * 50)

# Usando int(input()) para garantir que o valor seja um inteiro
n = int(input("Quantos alunos serão cadastrados? "))

# -----------------------------------------------------------------------------
# PASSO 2: LEITURA DOS DADOS (Loop for)
# -----------------------------------------------------------------------------
# Utilizando um laço for para iterar N vezes e coletar os dados
for i in range(n):
    print(f"--- Cadastro do Aluno {i + 1} ---")
    
    # Lendo o nome do aluno
    nome = input("Nome do Aluno: ")
    
    # Lendo as notas e convertendo para float
    nota1 = float(input("Nota 1 (N1): "))
    nota2 = float(input("Nota 2 (N2): "))
    
    # Armazenando no dicionário: chave = nome, valor = lista com as notas
    dados_alunos[nome] = [nota1, nota2]

# -----------------------------------------------------------------------------
# PASSO 3: PROCESSAMENTO E EXIBIÇÃO
# -----------------------------------------------------------------------------
print("=" * 60)
print("                    RELATÓRIO DE NOTAS")
print("=" * 60)

# Percorrendo o dicionário usando o método .items()
for nome, notas in dados_alunos.items():
    # Extraindo as notas da lista
    nota1 = notas[0]
    nota2 = notas[1]
    
    # CÁLCULO: Calculando a média simples
    media = (nota1 + nota2) / 2
    
    # CONDICIONAL: Determinando a situação do aluno
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
# RESUMO DA TURMA
# -----------------------------------------------------------------------------
aprovados = 0
reprovados = 0
sub = 0

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
```

---

## 5. Explicação dos Conceitos

### 5.1 Variáveis Utilizadas

| Variável | Tipo | Descrição |
|----------|------|-----------|
| `dados_alunos` | dict | Dicionário que armazena todos os alunos |
| `n` | int | Quantidade de alunos a cadastrar |
| `nome` | str | Nome do aluno (chave do dicionário) |
| `nota1`, `nota2` | float | Notas do aluno |
| `notas` | list | Lista contendo [nota1, nota2] |
| `media` | float | Média calculada do aluno |
| `situacao` | str | Situação final (Aprovado/Sub/Reprovado) |
| `aprovados` | int | Contador de alunos aprovados |
| `reprovados` | int | Contador de alunos reprovados |
| `sub` | int | Contador de alunos em sub |

### 5.2 Estruturas de Dados

**DICIONÁRIO (dict):**
- Estrutura que armazena pares chave:valor
- Exemplo: `dados_alunos = {"João": [7.5, 8.0], "Maria": [9.0, 8.5]}`
- Método `.items()` retorna tuplas (chave, valor) para iteração

**LISTA (list):**
- Estrutura ordenada e mutável
- Usada para armazenar as notas: `[nota1, nota2]`
- Acesso por índice: `notas[0]`, `notas[1]`

### 5.3 Operadores

**Aritméticos:**
| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `+` | Adição | `nota1 + nota2` |
| `/` | Divisão | `(nota1 + nota2) / 2` |
| `*` | Multiplicação | `"=" * 50` (repetição de string) |

**Comparação:**
| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `>=` | Maior ou igual | `media >= 60` |
| `<` | Menor que | `media < 30` |

**Atribuição:**
| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `=` | Atribuição simples | `dados_alunos = {}` |
| `+=` | Atribuição composta | `aprovados += 1` |

### 5.4 Estruturas de Controle

**LOOP FOR:**
- Usado para iterar um número determinado de vezes
- `for i in range(n):` itera de 0 até n-1
- `for nome, notas in dados_alunos.items():` itera sobre o dicionário

**CONDICIONAL IF-ELIF-ELSE:**
- Permite executar blocos de código baseado em condições
- `if`: primeira condição
- `elif`: condições alternativas
- `else`: caso nenhuma condição anterior seja verdadeira

### 5.5 Funções de Entrada/Saída

**input(mensagem):**
- Lê dados do teclado
- Retorna sempre uma string
- Deve ser convertido: `int(input(...))` ou `float(input(...))`

**print(valor):**
- Exibe dados na tela
- f-strings permitem formatação: `f"Média: {media:.2f}"`

---

## 6. Exemplo de Execução

```
==================================================
   SISTEMA DE GERENCIAMENTO DE NOTAS DE ALUNOS
==================================================

Quantos alunos serão cadastrados? 3

--- Cadastro do Aluno 1 ---
Nome do Aluno: João Silva
Nota 1 (N1): 7.5
Nota 2 (N2): 8.0

--- Cadastro do Aluno 2 ---
Nome do Aluno: Maria Santos
Nota 1 (N1): 4.0
Nota 2 (N2): 5.5

--- Cadastro do Aluno 3 ---
Nome do Aluno: Pedro Costa
Nota 1 (N1): 2.0
Nota 2 (N2): 1.5

============================================================
                    RELATÓRIO DE NOTAS
============================================================

Aluno: João Silva
  Notas: N1 = 7.5 | N2 = 8.0
  Média: 7.75
  Situação: Aprovado
----------------------------------------
Aluno: Maria Santos
  Notas: N1 = 4.0 | N2 = 5.5
  Média: 4.75
  Situação: Sub
----------------------------------------
Aluno: Pedro Costa
  Notas: N1 = 2.0 | N2 = 1.5
  Média: 1.75
  Situação: Reprovado
----------------------------------------

============================================================
                  RESUMO DA TURMA
============================================================
Total de Alunos: 3
Aprovados: 1
Em Sub: 1
Reprovados: 1
============================================================
```

---

## 7. Como Executar

```bash
python sistema_notas.py
```

---

## 8. Conclusão

Esta atividade demonstrou a aplicação prática dos seguintes conceitos de programação em Python:

- ✅ **ALGORITMOS:** Sequência lógica de passos para resolver o problema
- ✅ **FLUXOGRAMAS:** Representação visual do algoritmo
- ✅ **VARIÁVEIS:** Armazenamento de dados (inteiros, floats, strings)
- ✅ **OPERADORES:** Aritméticos (+, /) e de comparação (>=, <)
- ✅ **ESTRUTURAS DE CONTROLE:** Loops (for) e condicionais (if-elif-else)
- ✅ **ESTRUTURAS DE DADOS:** Dicionários e listas

O programa desenvolvido é funcional, bem organizado e segue as boas práticas de programação, incluindo comentários explicativos e formatação clara da saída.

---

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `sistema_notas.py` | Código fonte executável |
| `Documento_Atividade.txt` | Documentação completa em texto |
| `README.md` | Este arquivo |

---

**Autor:** Joabe Nascimento  
**Email:** joabefnascimento1@outlook.com

