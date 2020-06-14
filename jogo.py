import pygame
pygame.init()
x = 400
y = 300
velocidade = 15
fundo = pygame.image.load('rua.png')
carro = pygame.image.load('carro_AMARELO.png')

janela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('criando um jogo')

janela_aberta =True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x, y))
    pygame.display.update()

pygame.quit()