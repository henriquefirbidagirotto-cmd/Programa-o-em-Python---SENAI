# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
def display():
    try:
        n = int(input('Digite um numero:'))
        print(n)
    except ValueError as erro:
        print('erro')
    
    display ()
# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
def display():
    try:
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite um numero:'))
        n3 = (n1/n2)
        print(n3)
    except ValueError as erro:
        print('erro')
    except ZeroDivisionError as erro:
        print('erro')
display()
# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
def display():
    try:
        tr = str(input('Digite algo'))
        l = [tr]
        print(l)
    except ValueError as erro:
        print('erro')
    except ZeroDivisionError as erro:
        print(' erro')
    except SyntaxError as erro:
        print('erro no sistema tente novamente mais tarde')
display()