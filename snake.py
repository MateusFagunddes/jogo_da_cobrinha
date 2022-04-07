import pygame, random
from pygame.locals import *

# Funções de apoio
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Definição de macros para o movimento da cobrinha
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Cobrinha')
# gerar cobrinha
cobrinha = [(200, 200), (210, 200), (220,200)]
cobrinha_skin = pygame.Surface((10,10))
cobrinha_skin.fill((215,215,215)) #White

# gerar comidinha
comidinha_pos = on_grid_random()
comidinha = pygame.Surface((10,10))
comidinha.fill((0,150,0))

my_direction = DOWN

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(cobrinha[0], comidinha_pos):
        comidinha_pos = on_grid_random()
        cobrinha.append((0,0))
        score = score + 1

    # checa se a cobrinha bateu nas bordas
    if cobrinha[0][0] == 600 or cobrinha[0][1] == 600 or cobrinha[0][0] < 0 or cobrinha[0][1] < 0:
        game_over = True
        break

    # checa se a cobrinha bateu no próprio corpo
    for i in range(1, len(cobrinha) - 1):
        if cobrinha[0][0] == cobrinha[i][0] and cobrinha[0][1] == cobrinha[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1])

    # movimentando a cobrinha.
    if my_direction == UP:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if my_direction == DOWN:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if my_direction == RIGHT:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    if my_direction == LEFT:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    screen.fill((50,50,50))
    screen.blit(comidinha, comidinha_pos)

    for x in range(0, 600, 10): # linhas horizontais
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 600))
    for y in range(0, 600, 10): # linhas verticais
        pygame.draw.line(screen, (50, 50, 50), (0, y), (600, y))

    score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in cobrinha:
        screen.blit(cobrinha_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 20, 20))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600/2, 600/2-75)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(600)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
