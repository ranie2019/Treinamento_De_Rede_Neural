import pygame
from random import randint
pygame.init()
x = 380
y = 100
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 2500
timer = 0
tempo_segundo = 0

velocidade_outros = 12
velocidade = 10

fundo = pygame.image.load('rua.PNG')
carro = pygame.image.load('carro.png')
carro_branco = pygame.image.load('carro_branco.png')
carro_laranja = pygame.image.load('carro_laranja.png')
carro_vermelho = pygame.image.load('carro_vermelho.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 740:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 130:
        x -= velocidade

    # verifica a colisao
    if x + 80 > pos_x and y + 180 > pos_y:
        y = 1200

    if x - 80 < pos_x - 300 and y + 180 > pos_y_a:
        y = 1200

    if x + 80 > pos_x - 136 > x - 80 and y + 180 > pos_y_c and y + 180 > pos_y_c:
        y = 1200

    if pos_y <= -80:
        pos_y = randint(800,1000)

    if pos_y_a <= -80:
        pos_y_a = randint(1200, 2000)

    if pos_y_c <= -80:
        pos_y_c = randint(2200, 3000)

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y   -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_c -= velocidade_outros + 10


    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carro_branco, (pos_x + 140, pos_y))
    janela.blit(carro_laranja, (pos_x - 360, pos_y_a))
    janela.blit(carro_vermelho, (pos_x - 170, pos_y_c))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()