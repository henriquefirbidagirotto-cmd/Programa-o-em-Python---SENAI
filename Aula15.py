import pygame

pygame.init()

tela = pygame.display.set_mode((1920,1000))
pygame.display.set_caption('titulo')
run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False

    tela.fill('red')
    pygame.draw.rect(tela,'blue',(960,500,300,300))
    pygame.draw.ellipse(tela,'purple',(960,500,300,300))
    pygame.draw.circle(tela, ('black'), (10,20), 20)
    pygame.display.flip()

pygame.quit()