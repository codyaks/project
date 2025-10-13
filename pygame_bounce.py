import pygame
import random

pygame.init()
#costom event id
sprite_colour_event=pygame.USEREVENT+1
bg_colour_event=pygame.USEREVENT+2
#colur for bg
red=pygame.Color("red")
blue=pygame.Color("blue")
white=pygame.Color("white")
#colour for sprite
pink=pygame.Color("pink")
orange=pygame.Color("orange")
green=pygame.Color("green")
#create a class for sprite
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        side_hit=False
        if self.rect.right<=20 or self.rect.left>=480:
            self.velocity[0]=-self.velocity[0]
            side_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            side_hit=True
        if side_hit:
            pygame.event.post(pygame.event.Event(sprite_colour_event))
            pygame.event.post(pygame.event.Event(bg_colour_event))
    
    def change_sprite_colour(self):
        self.image.fill(random.choice([pink,orange,green]))
    
def change_bg_colour():
    global bg_colour
    bg_colour=(random.choice([blue,white,red]))
all_sprite_list=pygame.sprite.Group()
sp1=sprite(pink,30,40)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,380)
all_sprite_list.add(sp1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("bouncing sprite")
bg_colour=blue
screen.fill(bg_colour)
run=True
clock=pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==sprite_colour_event:
            sp1.change_sprite_colour()
        elif event.type==bg_colour_event:
            change_bg_colour()
    all_sprite_list.update()
    screen.fill(bg_colour)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)
pygame.quit()