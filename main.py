import pygame
import random

W = 800
H = 600

pygame.init()
pygame.display.set_caption("Текст")
pygame.display.set_mode((W,H))
screen = pygame.display.set_mode((W,H))
navy = (5, 0, 50)
screen.fill(navy)
pygame.mouse.set_visible(False)
font = pygame.font.SysFont('Arial', 38,True,False)
font2 = pygame.font.SysFont('Arial', 18,True,False)

text1 = font.render('Всем привет', 6, (360, 0,0))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
