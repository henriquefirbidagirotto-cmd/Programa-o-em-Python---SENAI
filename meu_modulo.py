import random
# **Crie um número aleatório de 5,10**

def ale():
    return random.randint(5,10)

# **2 - Crie 3 números aleatórios**
def ale1():
    return random.randint(5,10)

def ale2():
    return random.randint(5,10)

def ale3():
    return random.randint(5,10)
# **3 - Crie um número aleatório entre 10 a 30 utilize o range()**
def ale4():
    return random.randrange(10,30)
# **4 - Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
def cont():
   
    for c in range(10,0,-1):
        print(c)
    print('Fogo')
# **5 - Soma de números pares**
def soma():
    n1 = int(input('Digite um numero:'))
    n3 = int(input('Digite um numero:'))
    n2 = n1+n3
    n4 = n2%2
    if n4 == 0:
        print(n1,n3,'são numeros pares que da:',n2)
    else:
        print('so somamos numeros pares')
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
def us():
    nu1 = int(input('Digite um numero inteiro positivo'))
    if nu1 >=1:
        s = 0
        for m in range(2,nu1,2):
            s = s + m
           
        print(s,'positivo')
    else:
        print('tem que ser um numero inteiro!!!')
    