#Operadores aritméticos
#Todo mundo já usou operadores aritméticos na escola! Nos primeiros anos de estudo aprendemos a fazer continhas de soma,subtração,multiplicação e divisão.
# No Python também temos esses operadores e podemos realizar todos esses cálculos!

# Adição

print(10+20)
print(10+20+30+40+50+60+70+80+90+100)
print('Romulo tem ',2024-1984,'anos e Keity tem',2024-1995,'anos de idade')

# Subtração

print(10-20)
print('🍎🍎🍎🍎🍎🍎🍏🍏🍏🍏🍏🍏👦🏻💗👧🏻🍏🍏🍏🍏🍏🍏🍎🍎🍎🍎🍎🍎')
print('Eu tinha 5 maçãs e Keity comeu 2 maçãs com quantas ficamos? ','Assim que Keity comeu duas maçãs das 5 maçãs ficamos com ',5-2,'maçãs')
print('🍎🍎🍎🍎🍎🍎🍏🍏🍏🍏🍏🍏👦🏻💗👧🏻🍏🍏🍏🍏🍏🍏🍎🍎🍎🍎🍎🍎')

print('🎲🎲🎲🎲🪓🎲🎲🎲🎲⚔️🎲🎲🎲🧙🏻‍♂️🎲🎲🎲🪄🎲🎲🎲🎲🗡️🎲🎲🎲🎲')
print('Eu,Vitor,Ramon e Leir resolvemos jogar RPG e nosso grupo encontrou um Ogro com 150 pontos de vida
nosso grupo tomou a iniciativa e atacou causando Romulo 12 de dano,Vitor 13, Ramon 14 e Leir 15 então quanto foi o dano total?' , 'O ogro levou ',150-12-13-14-15,'pontos de dano')
print('🎲🎲🎲🎲🪓🎲🎲🎲🎲⚔️🎲🎲🧙🏻‍♂️🎲🎲🪄🎲🎲🎲🎲🗡️🎲🎲🎲🎲')
# Multiplicação

print(10*8)
print(12*3*5)
print('🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓')
print('Eu Romulo continuei meu ataque contra o ogro e tirei um 20 em minha rolagem acerto critico que é x3 com machado grande e ao rolar o d12 tirei 8 ,
Eu tenho bonus de força +5 e ao que no total meu ataque foi de : ' , 8*3+5,' de dano no ogro')
print('🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓')
# Divisão

print(10/2)
print('🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁')
print('Eu e Keity estavamos vendendo brigadeiros juntos cada um custava 2 reais e vendemos 47 brigadeiros então quanto foi o valor total de brigadeiros vendidos?', 
'Foram vendidos ao total ', 2*47,'reais em brigadeiros')
print('🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁🧁')

# Divisão com resultado inteiro
print('🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣')
print('Eu e Keity dessa vez estamos comendo hot philadelphia e queremos saber com quantos hots inteiros cada um vai comer? Normalmente eu como o dobro do que ela e a porção vem 60 hots.')
total_hots = 60
keity_hots = total_hots // 3  
romulo_hots = total_hots - keity_hots  
print('Então Romulo vai comer', romulo_hots, 'hots inteiros.')
print('E a porção que a Keity vai comer é', keity_hots, 'hots inteiros.')
print('🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣🍣🍱🥢🥢🍱🍣')

#Modulo
print('🎈🎈🎈🎈👦🏻🎈🎈🎈🎈👦🏻🎈🎈🎈🎈👧🏻🎈🎈🎈🎈👧🏻🎈🎈🎈🎈👧🏻🎈🎈🎈')
print('Resolvemos ir ao circo e Keity ganhou 23 balões para distribuir com nossas 5 crianças -Alicia,Celine,Daphine,Alzernando e Fernemir. 
Você quer saber quantos balões cada criança receberá e quantos balões sobrarão.')
total_baloes = 23
numero_criancas = 5
baloes_por_crianca = total_baloes // numero_criancas
baloes_sobrando = total_baloes % numero_criancas
print(f"Cada criança receberá {baloes_por_crianca} balões.")
print(f"Sobrarão {baloes_sobrando} balões.")
print('🎈🎈🎈🎈👦🏻🎈🎈🎈🎈👦🏻🎈🎈🎈🎈👧🏻🎈🎈🎈🎈👧🏻🎈🎈🎈🎈👧🏻🎈🎈🎈')

#Exponenciação
print('🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️')
print('Eu queria calcular a área de uma sala que é um quadrado. A fórmula para a área de um quadrado é lado elevado ao quadrado. Vamos usar a exponenciação para calcular isso.')
lado = 4
area = lado ** 2
print(f"A área da sala com lado {lado} metros é {area} metros quadrados.")
print('🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️')

# Fala, galera! Vamos fazer um resumão dos operadores aritméticos no Python de um jeito bem maneiro e fácil de entender. 
# Se liga só:

# 1. Adição (+)
# Todo mundo já fez soma na escola, né? No Python, é a mesma coisa! A gente usa o sinal de mais (+) para somar números.
# Exemplo:
print(10 + 20)  # Isso vai imprimir 30 na tela.
print(10 + 20 + 30 + 40 + 50 + 60 + 70 + 80 + 90 + 100)  # Soma de vários números!

# 2. Subtração (-)
# Subtração também é moleza! Usamos o sinal de menos (-) para subtrair.
# Exemplo:
print(10 - 20)  # Isso vai imprimir -10 na tela.
# Vamos usar um exemplo divertido com maçãs:
print('Eu tinha 5 maçãs e Keity comeu 2. Ficamos com', 5 - 2, 'maçãs.Eita Keity!')

# 3. Multiplicação (*)
# Multiplicar é só usar o asterisco (*). Fácil, né?
# Exemplo:
print(10 * 8)  # Isso vai imprimir 80 na tela.
# E se a gente estiver jogando RPG e quiser calcular o dano de um ataque crítico?
print('Meu ataque com machado grande causou', 8 * 3 + 5, 'de dano no ogro!E que pancada!')

# 4. Divisão (/)
# Para dividir, usamos a barra (/). Tranquilo!
# Exemplo:
print(10 / 2)  # Isso vai imprimir 5.0 na tela.
# E se estivermos vendendo brigadeiros?
print('Vendemos 47 brigadeiros a 2 reais cada. Total: ', 2 * 47, 'reais.', 'E se agora formos dividir o total do dinheiro pelos dois como ficaria?', 2 * 47 / 2, 'reais. Pegou a visão, né?')

# 5. Divisão Inteira (//)
# A divisão inteira é quando a gente quer o resultado sem as casas decimais. Usamos duas barras (//).
# Exemplo:
total_hots = 60
keity_hots = total_hots // 3  # Keity come 1/3 dos hots.
romulo_hots = total_hots - keity_hots  # Romulo come o resto.
print('Romulo vai comer', romulo_hots, 'hots inteiros.Eita nesse dia me dei bem!')
print('Keity vai comer', keity_hots, 'hots inteiros.Ela não gostava de comida japonesa no inicio do namoro com o Romulo. Hoje em dia casada ela come bem mais hots!')

# 6. Módulo (%)
# O módulo é o resto da divisão. Usamos o sinal de porcentagem (%).
# Exemplo:
total_baloes = 23
numero_criancas = 5
baloes_por_crianca = total_baloes // numero_criancas
baloes_sobrando = total_baloes % numero_criancas
print(f"Cada criança receberá {baloes_por_crianca} balões.")
print(f"Sobrarão {baloes_sobrando} balões.")

# 7. Exponenciação (**)
# Para elevar um número a uma potência, usamos dois asteriscos (**).
# Exemplo:
lado = 4
area = lado ** 2
print(f"A área de um quadrado com lado {lado} metros é {area} metros quadrados.")

# E aí, curtiram? Vimos como os operadores aritméticos são super úteis no Python e como podemos usá-los em várias situações do dia a dia.
# Agora é só praticar e se divertir com o Python! Valeu e até a próxima!
