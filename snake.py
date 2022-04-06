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
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da Cobrinha')
# gerar cobrinha
snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((215,215,215)) #White

# gerar comidinha
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((0,150,0))

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

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    # checa se a cobrinha bateu nas bordas
    if snake[0][0] == 500 or snake[0][1] == 500 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # checa se a cobrinha bateu no próprio corpo
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # movimentando a cobrinha.
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((50,50,50))
    screen.blit(apple, apple_pos)

    for x in range(0, 500, 10): # linhas horizontais
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, 500))
    for y in range(0, 500, 10): # linhas verticais
        pygame.draw.line(screen, (50, 50, 50), (0, y), (500, y))

    score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 20, 20))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (500/2, 500/2-75)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()