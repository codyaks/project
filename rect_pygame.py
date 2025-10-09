import pygame
pygame.init
scr_wd,scr_hg=300,300
screen=pygame.display.set_mode((scr_wd,scr_hg))
pygame.display.set_caption("rectange")
colour=pygame.Color('red')
wd,hg=100,60
done=True
clock=pygame.time.Clock()
while done:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            done=False
    screen.fill((0,0,1))
    pygame.draw.rect(screen,colour,(30,50,wd,hg))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()