import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Simple Paint")
clock = pygame.time.Clock()

color = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)  # red
            elif event.key == pygame.K_g:
                color = (0, 255, 0)  # green
            elif event.key == pygame.K_b:
                color = (0, 0, 255)  # blue
            elif event.key == pygame.K_c:
                screen.fill((255, 255, 255))  #white

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, pos, 5)

    pygame.display.flip()
    clock.tick(60)
