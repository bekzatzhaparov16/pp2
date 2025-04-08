import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 60)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GOLD = (255, 215, 0)

bg = pygame.image.load("AnimatedStreet.png")
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")
crash_sound = pygame.mixer.Sound("crash.wav")

score = 0
level = 1
enemy_speed = 5
coins_collected = 0
COINS_TO_LEVEL_UP = 5

player = player_img.get_rect(center=(160, 520))
enemy = enemy_img.get_rect(center=(random.randint(40, WIDTH - 40), 0))

def create_coin():
    radius = random.randint(10, 20)
    x = random.randint(40, WIDTH - 40)
    y = random.randint(100, HEIGHT - 100)
    return pygame.Rect(x, y, radius * 2, radius * 2), radius

coin, coin_radius = create_coin()
\
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0: player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH: player.x += 5
    if keys[pygame.K_UP] and player.top > 0: player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT: player.y += 5

    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy.y = 0
        enemy.centerx = random.randint(40, WIDTH - 40)

    if player.colliderect(enemy):
        crash_sound.play()
        screen.fill(RED)
        game_over = big_font.render("Game Over", True, BLACK)
        screen.blit(game_over, (50, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit(); sys.exit()

    if player.colliderect(coin):
        score += coin_radius
        coins_collected += 1
        coin, coin_radius = create_coin()
        if coins_collected >= COINS_TO_LEVEL_UP:
            coins_collected = 0
            level += 1
            enemy_speed += 1

    screen.blit(bg, (0, 0))
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    pygame.draw.circle(screen, GOLD, coin.center, coin_radius)
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 30))

    pygame.display.update()
    clock.tick(60)
