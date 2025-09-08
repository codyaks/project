import pygame
pygame.init()
sw,sh=500,500
display_surface=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("adding image and background image")
bg=pygame.transform.scale(pygame.image.load("img.png").convert(),(sw,sh))
pimg=pygame.transform.scale(pygame.image.load("pyimg.jpg").convert(),(250,250))
prect=pimg.get_rect(center=(sw//2,sh//2))

def gameloop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(bg,(0,0))
        display_surface.blit(pimg,prect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
gameloop()