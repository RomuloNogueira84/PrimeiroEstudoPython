# Manipulação de Strings

# split() é usado para dividir uma string em partes
frase = "Estou buscando aprender Python"
frase.split()

frase = "Estou buscando aprender Python.Quero me tornar um desenvolvedor"
print(frase.split())
print(frase.split('.'))

oracao = "Pai, eu Te agradeço por todas as bênçãos de prosperidade e abundância que derramaste sobre a minha vida. Eu sei que posso confiar em Ti para suprir todas as minhas necessidades, seja material, emocional ou espiritual. Abro meu coração e minha mente para receber a abundância que tens para mim. Amém."
print(oracao.split())
print(oracao.split('.'))

# strip() é usado para remover espaços em branco do inicio e do final da string
estudo = "         Python é uma linguagem de programação que é muito popular entre os programadores.      "
estudo = (estudo.strip())
print(estudo)

# Capitalize() é usado para transformar a primeira letra de cada palavra em maiúscula
nome = "romulo"
sobrenome = "nogueira"
nome = nome.capitalize()
sobrenome = sobrenome.capitalize()
nome_completo = nome + " " + sobrenome
print(nome)
print(sobrenome)
print(nome_completo)

# lower() é usado para transformar todas as letras em minúsculas
nome = "ROMULO"
nome = nome.lower()
print(nome)

# upper() é usado para transformar todas as letras em maiúsculas
nome = "romulo"
nome = nome.upper()
print(nome)


nome = "romulo"
sobrenome = "nogueira"
ultimo_sobrenome = "de souza"
nome = nome.capitalize()
sobrenome =  sobrenome.upper()
ultimo_sobrenome = ultimo_sobrenome.lower()


print(f"Meu nome completo é {nome} {sobrenome} {ultimo_sobrenome}")


# Title() é usado para transformar a primeira letra de cada palavra em maiúscula e todas as outras letras em minúsculas
nome = "romulo"
sobrenome = "nogueira"
ultimo_sobrenome = "de souza"

nome = nome.title()
sobrenome = sobrenome.title()
ultimo_sobrenome = ultimo_sobrenome.title()

print(f"Meu nome completo é {nome} {sobrenome} {ultimo_sobrenome}")

filme = "The Lord of the Rings: The Fellowship of the Ring"
filme = filme.title()
print(filme)

filme = "the lord of the rings: two towers"
filme = filme.title()
print(filme)

filme = "the lord of the rings: Return of the King"
filme = filme.title()
print(filme)


