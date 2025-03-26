import pygame
import time
from datetime import datetime

pygame.init()

clock_img = pygame.image.load("clock.png")
minute_hand_img = pygame.image.load("min_hand.png")
second_hand_img = pygame.image.load("sec_hand.png")

clock_rect = clock_img.get_rect()
WIDTH, HEIGHT = clock_rect.width, clock_rect.height

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

center_x, center_y = WIDTH // 2, HEIGHT // 2


def rotate_image(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    minute_angle = (minutes % 60) * 6
    second_angle = (seconds % 60) * 6

    min_hand_rotated, min_hand_rect = rotate_image(minute_hand_img, minute_angle, (center_x, center_y))
    sec_hand_rotated, sec_hand_rect = rotate_image(second_hand_img, second_angle, (center_x, center_y))

    screen.blit(min_hand_rotated, min_hand_rect.topleft)
    screen.blit(sec_hand_rotated, sec_hand_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)  

pygame.quit()
