import random
import time
from tkinter import *
from tkinter import messagebox

import pygame

Tk().wm_withdraw()
count, n = 0, False

a = [i for i in range(100)]
lin = random.choice(a)

lint = 'https://' + str(lin) + '/error/Vam/' + str(lin) + '/Cones'

pygame.init()

screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption('error')
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render('hahahahhha', 1, (12, 140, 0, 1))

while True:
    if not n:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                count += 1
                pygame.quit()
                time.sleep(0.10)
                screen = pygame.display.set_mode((800, 200))
                pygame.display.set_caption('Error')
                messagebox.showerror('Error', 'hahahahah')
            if count == 9:
                n = True
                break
    else:
        break

    screen.fill((0, 0, 0))
    screen.blit(label, (50, 50))
    pygame.display.update()
