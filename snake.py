import pygame, sys, random, time

pygame.init()
CELL = 20
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]
direction = (CELL, 0)
score = 0
level = 1
speed = 10

def new_food():
    while True:
        weight = random.randint(1, 3)
        x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL
        if (x, y) not in snake:
            return (x, y), weight

food, food_weight = new_food()
food_time = time.time()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL): direction = (0, -CELL)
    if keys[pygame.K_DOWN] and direction != (0, -CELL): direction = (0, CELL)
    if keys[pygame.K_LEFT] and direction != (CELL, 0): direction = (-CELL, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL, 0): direction = (CELL, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head in snake or not (0 <= head[0] < WIDTH) or not (0 <= head[1] < HEIGHT):
        pygame.quit(); sys.exit()
    snake.insert(0, head)

    if head == food:
        score += food_weight
        if score // 3 + 1 > level:
            level += 1
            speed += 2
        food, food_weight = new_food()
        food_time = time.time()
    else:
        snake.pop()

    if time.time() - food_time > 5:
        food, food_weight = new_food()
        food_time = time.time()

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

    pygame.draw.circle(screen, RED, (food[0] + CELL // 2, food[1] + CELL // 2), food_weight * 5)

    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 30))

    pygame.display.update()
    clock.tick(speed)
