import pygame
win=pygame.display.set_mode((1000,500))
run=1

x=250
y=250

class rc :
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("Black_viper.png"),(128,128))
        self.surr = self.img.get_rect()
    def move(self,inp):
        win.blit(self.img,(self.surr.x,250))
        if inp[pygame.K_LEFT]:
            self.surr.x-=1
        if inp[pygame.K_RIGHT]:
            self.surr.x+=1

temp=rc()
temp.surr.x=0
temp.surr.y=250
car_mask=pygame.mask.from_surface(temp.img)

class vehicle:
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("taxi.png"),(128,128))
        self.surr = self.img.get_rect()
    def move(self,inp):
        win.blit(self.img,(self.surr.x,250))
        if inp[pygame.K_a]:
            self.surr.x-=1
        if inp[pygame.K_b]:
            self.surr.x+=1
dis=vehicle()
dis.surr.x = 600
dis.surr.y = 250
lorry_mask=pygame.mask.from_surface(dis.img)

while run:

    pygame.display.update()
    inp=pygame.key.get_pressed()

    temp.move(inp)

    dis.move(inp)

    pygame.draw.rect(win,(250,250,250),(temp.surr.x,temp.surr.y,20,20))

    if(car_mask.overlap(lorry_mask,(dis.surr.x-temp.surr.x , dis.surr.y-temp.surr.y))):
        run=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0

    pygame.time.delay(10)