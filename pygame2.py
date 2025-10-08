import pygame
def main():
    pygame.init()
    scr_width,scr_height=500,500
    screen=pygame.display.set_mode((scr_width,scr_height))
    pygame.display.set_caption('colour changing sprite')
    
    colour={
        'red':pygame.Color('red'),
        "blue": pygame.Color("blue"),
        "white": pygame.Color("white"),
        "purple": pygame.Color("purple")
    }
    current_colour=colour['white']
    x,y=30,40
    sprite_wd,sprite_hg=60,60

    clock=pygame.time.Clock
    done=True
    
    while done:
        for event in pygame.event.get():
            if event.type==pygame.quit():
                done=False
        preesd=pygame.key.get_pressed()
        if[preesd==pygame.K_LEFT]:x-=3
        if[preesd==pygame.K_RIGHT]:x+=3
        if[preesd==pygame.K_UP]:y-=3
        if[preesd==pygame.K_DOWN]:y+=3
        x=min(max(0,x),scr_width-scr_width)
        y=min(max(0,y),scr_height-sprite_hg)
        if x==0: current_colour=colour["blue"]
        elif x==scr_width-sprite_wd: current_colour=colour["red"]
        elif y==0: current_colour=colour["purple"]
        elif x==scr_height-sprite_hg: current_colour=colour["white"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_colour,x,y,sprite_wd,sprite_hg)

        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
     main()