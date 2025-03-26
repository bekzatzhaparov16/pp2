import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = "music"
playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

def draw_screen(message):
    screen.fill((0, 0, 0))
    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (20, HEIGHT // 2 - 20))
    pygame.display.flip()

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    message = f"Playing: {os.path.basename(playlist[current_track])}"
    draw_screen(message)
    print(message)

def stop_music():
    pygame.mixer.music.stop()
    draw_screen("Music Stopped")
    print("Music stopped")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

if playlist:
    play_music()
else:
    draw_screen("No music files found")
    print("No music files found in the 'music' folder.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()

pygame.quit()
