# #Atividade 1:

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
# c = 1000
# while c > 0:
#     print(c)
#     c = c - 1
# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.
# for n1 in range(10):
#     n1 = input('Nome:')
#     print(n1)

# lista_nome = []
# quantidade = 10
# while quantidade > 0:
#     n1 = input('Nome:')
#     lista_nome.append(n1)
#     quantidade = quantidade -1
# print(lista_nome)


#Atividade 2:


## Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)
chance = 3


while chance > 0:
    senha = int(input('digite a senha'))
    if senha == 10:
  
        nota = float(input('insira a nota:'))
        print('insira a nota',nota)
        chance = chance -3
    elif senha != 10:
        print('senha incorreta')
        chance = chance -1