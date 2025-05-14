import pygame

from compute import compute_next_state

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 20
LINE_WIDTH = 1
SQUARES_X = SCREEN_WIDTH // SQUARE_SIZE
SQUARES_Y = SCREEN_HEIGHT // SQUARE_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
game_active = True
initial_time = pygame.time.get_ticks()

current_state = []

for i in range(SQUARES_X):
    row = []
    for j in range(SQUARES_Y):
        row.append(0)
    current_state.append(row)

for i in range(0, SCREEN_WIDTH, SQUARE_SIZE):
    pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, SCREEN_HEIGHT))
for i in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
    pygame.draw.line(screen, (0, 0, 0), (0, i), (SCREEN_WIDTH, i))

hasGameStarted = False

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hasGameStarted = not hasGameStarted 
        if event.type == pygame.MOUSEBUTTONDOWN and not hasGameStarted:
            x, y = event.pos
            x = x // SQUARE_SIZE
            y = y // SQUARE_SIZE
            if current_state[x][y] == 0:
                current_state[x][y] = 1
            else:
                current_state[x][y] = 0
    for i in range(SQUARES_X):
        for j in range(SQUARES_Y):
            if current_state[i][j] == 1:
                color = (0,0,0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, (i * SQUARE_SIZE + LINE_WIDTH, j * SQUARE_SIZE + LINE_WIDTH, SQUARE_SIZE - 2 * LINE_WIDTH, SQUARE_SIZE - 2 * LINE_WIDTH))
        

    pygame.display.update()
    pygame.display.update()
    if hasGameStarted:
        current_state = compute_next_state(current_state)
        pygame.time.delay(1000)
    clock.tick(60)

pygame.quit()