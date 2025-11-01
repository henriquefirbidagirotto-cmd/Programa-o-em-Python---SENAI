# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
s1 = int(input('Digite um numero'))
print(s1)

if s1 >0:
    print('positivo')
elif s1 == 0:
    print('é 0')
else:
    print('negativo')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('Qual sua idade?'))
if idade >= 16:
    print('Você pode votar')
elif idade <= 15:
    print('Você não pode votar')
# 3*

# Declara uma variável com um número qualquer, 
#determine se um número é par ou ímpar.
n10 = int(input('Digite um numero'))
print(n10)
if n10%2 == 0:
    print('par')
else:
    print('impar')
# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
n1 = int(input('Digite um numero'))
n2 = int(input('Digite um numero'))
n3 = int(input('Digite um numero'))
print(n1,n2,n3)

if n1 == n2 == n3:
    print('equilátero')
elif n1 == n2 or n3 == n2 or n1 == n3:
    print('isósceles')
else:
    print('escaleno')
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.
if 5%7 == 0:
    print('multiplo')
else:
    print('não e multiplo')
# 6*

# Verifique se um número é positivo e maior que 10
n22 = int(input('Digite um numero'))
if n22 >=1:
    print('Positivo')
if n22 >=10:
    print('É maior que 10')
else:
    print('Não e maior que 10')
# 7*

# Verifique se um número é divisível por 3 ou 5.
if 3%5 == 0:
    print('divisivel')
else:
    print('Não é divisivel')