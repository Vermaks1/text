import pygame
pygame.init()
 
sc = pygame.display.set_mode((800,600))
sc.fill((5,0,50))
 
f1 = pygame.font.Font(None, 60)
text1 = f1.render('Всем привет', 5, (255,255,255))
 
f2 = pygame.font.SysFont(None, 36)
text2 = f2.render("задание на урок", 1, (255,0,0))

pygame.draw.rect(sc, (255, 0, 0), (370, 240, 45, 45))
 
sc.blit(text1, (270, 300))
sc.blit(text2, (300, 350))
 
pygame.display.update()
 
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            exit()
