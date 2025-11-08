# variáveis locais, globais e parâmetros

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS par ou impar. UTILIZE VARIÁVEIS LOCAIS.***

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = n1%2
n4 = n2%2
def display():
    if n3 == 0:
        print('par')
    else:
        print('impar')
    if n4 == 0:
        print('par')
    else:
        print('impar')
display()
# ***2***

# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***
nu1 = int(input('Digite um numero:'))
nu2 = int(input('Digite um numero:'))
nu3 = int(input('Digite um numero:'))
nu4 = nu1 * nu2 * nu3
print(nu4)
# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***
num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero que vc vai querer que eleve o primeiro:'))
num3 = num1 ** num2
print(num3)
# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***
nume = int(input('Digite sua idade:'))
if nume == 18:
    print('você é grandinho')
else:
    print('você ou e velhinho ou e bebezinho')
# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***
num1 = int(input('qual ano você nasceu:'))
num2 = 2025 - num1
print(num2)
# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***
print('responda com s ou n')
nume = str(input('O Brasil ganhou a copa de 1999?'))
if nume == 's':
    print('você errou a copa do mundo acontece de 4 em 4 anos')
elif nume == 'n':
    print('Você acertou!!!')
else:
    print(' se sim = s, não = n')
# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***
def restaurante():
    print(f'''
    Cardápio
        
    opções de comidas
    Salada
    macarronada
    sanduiche
    ''')
    p = str(input('o que você deseja?'))
    if p == 'Salada':
        print('sua salada está sendo prepara')
    elif p == 'Salada e macarronada':
        print('sua salada e sua macarronada está sendo prepara')
    elif p == 'Salada, macarronada e sanduiche':
        print('sua salada, macarronada e sanduiche está sendo prepara')
    elif p == 'macarronada e Salada':
        print('sua salada e sua macarronada está sendo prepara')
    elif p == 'macarronada, Salada e sanduiche':
        print('sua salada, macarronada e sanduiche está sendo prepara')
    else:
        print('Peça do seguindo modelo:Salada, macarronada e sanduiche')

    p2 = str(input('Deseja pedir uma sobremesa?'))
    if p2 == 's':
        print('''
        sobremesas:
        
        sorvete
        pudin
        petit gateau
        ''')
        
        p3 = str(input('Qual sobremesa Gostaria?'))
        if p3 == 'sorvete':
            print('seu sorvete está sendo prepara, obrigado volte sempre')
        elif p3 == 'petit gateau e pudin':
            print('seu pudin e seu petit gateau está sendo prepara, obrigado volte sempre')
        elif p3 == 'sorvete, pudin e petit gateau':
            print('seu sorvete, pudin e petit gateau está sendo prepara, obrigado volte sempre')
        elif p3 == 'sorvete e petit gateau':
            print('seu  petit gateau e sua sorvete está sendo prepara, obrigado volte sempre')
        elif p3 == 'pudin, sorvete e petit gateau':
            print('seu sorvete, pudin e petit gateau está sendo prepara, obrigado volte sempre')
        else:
            print('Peça do seguindo modelo:sorvete, pudin e petit gateau')
    else:
        print('obrigado volte sempre')
restaurante()