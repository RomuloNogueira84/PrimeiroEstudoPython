# Trabalhando com variáveis
#Variáveis são um dos recursos mais básicos das linguagens de programação.
#  Através da utilização de variáveis, podemos armazenar dados na memória do computador para acessa-los mais tarde,quando forem necessários.
#Declaração e atribuição de variáveis
# Algumas regras devem ser seguidas ao criarmos um nome para uma variável:
# 1- precisa começar com uma letra ou um underscore
# 2- não pode começar com um número
# 3- não pode conter caracteres especiais (*, $, %, #, @...etc...)
# 4- nomes de variáveis são case sensitives (nome é diferente de Nome)
# 5- não pode ser uma palavra reservada da linguagem

nome_aluno = "Romulo"
print(nome_aluno)

ano_de_nascimento_Romulo = 1984


Nome_aluno = "Keity"
ano_de_nascimento_Keity = 1995

print(nome_aluno)
print(Nome_aluno)
print(ano_de_nascimento_Romulo)
print(ano_de_nascimento_Keity)

# Tipos de variáveis
# Inteiros

numero_telefone = 21987654321 
type(numero_telefone)

numero_cpf = 47446578901
type(numero_cpf)

#Floats
altura = 1.87
peso = 98.9
type(altura)
type(peso)

# Strings

frase = "Estou buscando aprender Python"
type(frase)

basico_string = "Uma string é simplesmente uma sequência de caracteres. Você pode criar uma string em Python usando aspas simples  ou duplas "

type(basico_string)

#Booleanos
verdadeiro = True
falso = False
type(verdadeiro)
type(falso)

status = True
type(status)

# Exercícios
ano_atual = 2024
nascimento_romulo = 1984
nascimento_keity = 1995
idade_romulo = ano_atual - nascimento_romulo
idade_keity = ano_atual - nascimento_keity
print(idade_romulo)
print(idade_keity)

diferenca_idade = idade_keity - idade_romulo
print(diferenca_idade)

romulo_torce_para = "Flamengo"
ano_de_fundacao_flamengo = 1895
print(f"O Flamengo foi fundado em {ano_de_fundacao_flamengo} e tem { ano_atual - ano_de_fundacao_flamengo } anos de fundação")

romulo_horas_trabalhada_hora_mes = 220
romulo_hora_dia = 8
dias_em_um_mes = romulo_horas_trabalhada_hora_mes / 8
print(f"Em um mês, o Romulo trabalha {romulo_horas_trabalhada_hora_mes} horas em {dias_em_um_mes} dias")

# Variáveis são como os guarda-sóis na praia: você coloca um ali, guarda suas coisas e depois volta pra pegar quando precisar. Elas são um dos recursos mais básicos das linguagens de programação, permitindo que a gente armazene dados na memória do computador para usar mais tarde.

