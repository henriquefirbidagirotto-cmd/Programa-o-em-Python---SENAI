# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

#Está importando as propriedades da biblioteca pygame
import pygame

# Inicializa o Pygame

#inicia a estrutura do codigo necessario para ele funcionar
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/



#é uma variavel atribuida para o tamanho da tela
largura, altura = 400, 400
#A variavel acessa a documentação pygame e chama os submodulo do documento e coloca o tamanho da tela com set_mode usando a variavel largura e altura.
tela = pygame.display.set_mode((largura, altura))
#acessa a documentação pygame e chama os submodulo do documento e coloca o tipo do jogo.
pygame.display.set_caption("Labirinto")

#variavel atribuida as propriedades do preto
preto = (0, 0, 0)
#variavel atribuida as propriedades do branco
branco = (255, 255, 255)
#variavel atribuida as propriedades do vermelho
vermelho = (255, 0, 0)

#variavel atribuida como tamanho_celula com tamanho 40
tamanho_celula = 40
#uma lista com propriedades boleanas, 1 é para saber aonde vai ter colisão e 0 aonde vai ser o caminho do labirinto.
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#duas variaveis que estão multiplicando 1 com a variavel tamanho celula
x, y = 1 * tamanho_celula, 1 * tamanho_celula
#variavel atribuida as propriedades da velocidade de algo.
velocidade = 40

# um 'chat local'
def desenhar_labirinto():
    #um loop atribuido a linha para ler labirinto no nome do jogo ao inicialo.
    for linha in range(len(labirinto)):
        #um loop para o codigo repetir varias vezes o nome labirinto na linha.
        for coluna in range(len(labirinto[linha])):
            #a variavel com nome cor tem a variavel que esta em chat global preto aonde tem as propriedade da cor em questão.
            #se labirinto[linha][coluna] for igual à 1 e para ter colisão, caso ao contrário será branco para sem colisão aonde o 'boneco' vai andar. 
            cor = preto if labirinto[linha][coluna] == 1 else branco
            #está atribuindo todas as formas da lista em retangulos e ajutando o tamanho de cada 0,1.
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

#variavel boleana que quando estiver sendo executado será verdadeiro.
executando = True
#loop da variavel boleana que enquanto estiver verdadeira ela vai se repetir caso ao contrário ela não será executada.
while executando:
    #loop que chama os modulos dizendo que se evento.type for igual a pygame.quit a varivel boleana será falsa então terminara o codigo 
    #então enquanto o executando for verdadeiro estará sendo executado o codigo do jogo.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    #aqui está sendo coloca o que cada uma das teclas vão fazer e o tanto de velocidade cade uma delas vao ter.
    #exemplo: na primeira ele esta colocando o a para se mover a esquerda com a velocidade da variavel que é 40 sabendo que cara quadrado tem 40 pixels cada vez que apertar 
    # a vai andar 1 casa a esquerda aonde tem a boleana 0 = false aonde n tem colisão assim que o 'personagem' encosta na boleana verdadeira (1) ele relaciona como uma parede
    #fazendo que não consiga andar.
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    #está colocando a boleana 0 branca.
    tela.fill(branco)

    #ele esta fechando o chat local do def.
    desenhar_labirinto()
    #está dando a cor ao personagem e colocando tamanho de x e y largura/altura.
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    #está fechando os modulos
    pygame.display.flip()

    #FPS
    pygame.time.Clock().tick(10)

#está falando que se apertar no x o jogo será fechado. 
pygame.quit()
