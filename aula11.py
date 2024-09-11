#Slicing
#Slicing é a extração de partes de uma sequência de caracteres, de forma que você possa extrair uma parte específica de uma string, lista ou tupla.

frase = "Estou buscando aprender Python"
# acessando o caractere de índice 0
print(frase[0])
# acessando o caractere de índice 1
print(frase[1])
# acessando o caractere de índice 2
print(frase[2])
# acessando o caractere de índice 11
print(frase[11:18])

# Steps de slicing
frase = "Estou buscando aprender Python"
print(frase[0:11:2])

# Invertendo uma string com slicing
frase = "Estou buscando aprender Python"
print(frase[::-1])
