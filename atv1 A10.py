# ***EXERCÍCIOS com match/ case:*** 

# ***1: Verificando se o número é par ou ímpar***
n = int(input('Digite um numero'))
s = n%2
match s:
    case 0:
        print('par')
    case 1:
        print('impar')
# ***2: Verificando se um número é positivo, negativo ou zero***
n1 = int(input('Digite um numero'))

match n1:
    case n1 if n1 > 0 :
        print('positivo')
    case n1 if n1 < 0 :
        print('negativo')
    case n1 if n1 == 0:
        print('zero')

# ***3: Verificando se uma string é vazia ou não***
st = input('Digete algo')
match st:
    case st if st == '':
        print('está vazia')
    case st if st > '':
        print('você digitou')


# ***4: Verificando se um número é maior, menor ou igual a 10***
p1 = int(input('Digite um numero:'))

match p1:
    case p1 if p1 > 10:
        print('é maior que 10')
    case p1 if p1 < 10:
        print('é menor que 10')
    case p1 if p1 == 10:
        print('é igual a 10')
# ***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***
idade = int(input('Digite sua idade:'))
match idade:
    case idade if idade <13:
        print('criança')
    case idade if idade >13 and idade <18:
        print('adolecente')
    case idade if idade >=18 and idade <35:
        print('jovem')
    case idade if idade >35 and idade <64:
        print('adulto')
    case idade if idade >65:
        print('idoso')