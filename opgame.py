import pygame,random
pygame.init()
clock=pygame.time.Clock()
win = pygame.display.set_mode((840,650))
back=pygame.transform.scale(pygame.image.load("background-1.png"),(840,650))
rc=pygame.transform.scale(pygame.image.load("Black_viper.png"),(128,128))
vehicle_path=["final truck.png",]
lorry=pygame.transform.scale(pygame.image.load(random.choice(vehicle_path)),(128,128))
i=0
q=0
run=1
t,c=10,0
class Race_car:
    def __init__(self,x):
        self.x=x
        self.vel=5
    def move(self,inp):
        win.blit(rc,(self.x,530))
        if inp[pygame.K_LEFT] and self.x>145:
            self.x-=self.vel
        elif inp[pygame.K_RIGHT] and self.x<580:
            self.x+=self.vel
class Vehicle:
    def __init__(self,y):
        self.x=(random.randint(29,116))*5
        self.y=y
        self.vel=2
    def move(self,y):
        win.blit(lorry,(self.x,self.y))
        self.y+=self.vel


player=Race_car(175)

disturbance=Vehicle(100)

while run:


    inp=pygame.key.get_pressed()

    win.blit(back,(0,i))
    win.blit(back,(0,i-650))

    i+=10
    if i==650:
        win.blit(back, (0, i - 650))
        i=0


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
    player.move(inp)
    disturbance.move(0)


    pygame.display.update()