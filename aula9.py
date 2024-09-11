# f-strings
# Também chamadas de strings literais formatadas (formatted string literals), f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de variáveis ou expressões.

idade = 40
peso = 98.5
altura = 1.87

print(f"Meu nome é Romulo e tenho {idade} anos")
print(f"Meu peso é {peso} kg e minha altura é {altura} m")

jogador1 = "Romulo"
jogador2 = "Vitor"
jogador3 = "Leir"
jogador4 = "Ramon"

jogadores = [jogador1, jogador2, jogador3, jogador4]

print(f"Os jogadores são {jogadores}")
print(f"O grupo é formado {jogador1} é um clérigo, {jogador2} é um ladino, {jogador3} é um barbaro e {jogador4} é um guerreiro")