import pygame
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

fs = 44100
seconds = 5
minus_file = "minus.mp3"

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Karaoke Recorder38")
font_main = pygame.font.Font(None, 36)

under_button_rect = button_rect = pygame.Rect(130, 105, 150, 125)
under_button_rect_color = (20,110,20)
button_rect = pygame.Rect(125, 100, 150, 125)
button_color = (20,150,20)
text_record = font_main.render("ЗАПИС", True, (255,255,255))

def start_karaoke():
    print("Recording right now...")

    try:
        pygame.mixer.music.load(minus_file)
        pygame.mixer.music.play()
    except:
        print("Minus file is not found")

    my_voice = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    pygame.mixer.music.stop()
    print("Recording is stopped")

    wav.write("voice_record.wav", fs, my_voice)
    print("File is waved as voice_record.wav")

running = True
while running:
   screen.fill((20, 20, 20))


   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False


       if event.type == pygame.MOUSEBUTTONDOWN:
           if button_rect.collidepoint(event.pos):
               button_color = (150, 20, 20)
               under_button_rect_color = (110, 20, 20)
               pygame.display.update()
               start_karaoke()
               button_color = (20, 150, 20)
               under_button_rect_color = (20, 110, 20)


   #малюємо кнопку
   pygame.draw.rect(screen, under_button_rect_color, under_button_rect, border_radius=10)
   pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
   screen.blit(text_record, (button_rect.x + 35, button_rect.y + 40))


   pygame.display.update()


pygame.quit()