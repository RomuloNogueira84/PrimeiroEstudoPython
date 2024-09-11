# Listas
# Uma lista é uma estrutura de dados composta por itens organizados de forma linear, na qual cada um pode ser acessado a partir de um índice, que representa sua posição na coleção (iniciando em zero).

# são mutáveis
# podem conter tipos diferentes de objetos

lista = ['Romulo' , 'Keity' , 'Janaina']
print(lista)
print(type(lista))

# Lista com tipo de objetos diferentes
lista_de_tudo = ['Romulo' , 1 , 2.5, 'Janaina' , True]
print(lista_de_tudo)

print(type(lista_de_tudo))

# Acessando elementos de uma lista pelo índice
Lista = ['Romulo','Desenvolvedor de sistemas' , 'Keity' , 'Governanta residencial' , 'Janaina' , 'Técnica de enfermagem']

print(Lista[0])
print(Lista[1])
print(Lista[2])

# Acessando uma lista dentro de uma lista ou lista com sublistas
lista_com_sublista = ['Romulo', 'Desenvolvedor de sistemas', 'Keity', 'Governanta residencial', 'Janaina', 'Técnica de enfermagem', [1, 2, 3, 4, 5]]
print(lista_com_sublista[6][1])
print(lista_com_sublista[6][2])