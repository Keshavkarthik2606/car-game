import pygame,random
from pygame import mixer

pygame.init()
mixer.init()
clock=pygame.time.Clock()
win = pygame.display.set_mode((840,650))
back=pygame.transform.scale(pygame.image.load("background-1.png"),(840,650))
vehicle_path=["final truck.png","Ambulance.png","final car.png","Mini_van final.png","Police final.png","taxi.png"]
font=pygame.font.Font(None,36)
back_end=pygame.transform.scale(pygame.image.load("image.png"),(840,650))
wrong=pygame.image.load("wrong lane.png")
racing=pygame.image.load("racing.png")
press=pygame.image.load("space.png")
game_over=pygame.image.load("game over.png")

i=0
q=0
score=0
count=1
temp=0
bgY=0
acceleration = 0.1
velocity = 2
maxspeed = 15
x_path=[133,190,255,310,380,435,490,540,595,]
coin_path=[190,230,320,470,500,525,570,600,630,]
overall=1
starter=0


flag=0
run=1
t,c=10,0
class Race_car:
    def __init__(self):
        self.vel=5
        self.car=pygame.transform.scale(pygame.image.load("Black_viper.png"),(128,128))
        self.surr = self.car.get_rect()
    def move(self,inp):
        win.blit(self.car,(self.surr.x,530))
        if inp[pygame.K_LEFT] and self.surr.x>150:
            self.surr.x-=self.vel
        elif inp[pygame.K_RIGHT] and self.surr.x<575:
            self.surr.x+=self.vel
player = Race_car()
player.surr.x= 175
player.surr.y=530
player_mask = pygame.mask.from_surface(player.car)

class Vehicle:
    def __init__(self):
        self.lorry = pygame.transform.scale(pygame.image.load(random.choice(vehicle_path)), (128, 128))
        self.surr = self.lorry.get_rect()
        self.vel=velocity
        self.acc = acceleration + 0.05
    def move(self,y):

        win.blit(self.lorry,(self.surr.x,self.surr.y))
        self.surr.y+=self.vel
        if self.vel<maxspeed:
            self.vel+=self.acc

disturbance=Vehicle()
disturbance.surr.x=(random.choice(x_path))
disturbance.surr.y=-128
dis_mask = pygame.mask.from_surface(disturbance.lorry)

class point:
    def __init__(self):
        self.img=pygame.transform.scale(pygame.image.load("coin1-removebg-preview.png"),(19,19))
        self.surr=self.img.get_rect()
        self.vel = velocity
        self.acc = acceleration + 0.05
    def move(self):
        win.blit(self.img,(self.surr.x,self.surr.y))
        self.surr.y += self.vel
        if self.vel < maxspeed:
            self.vel += self.acc
coin = point()
coin.surr.x=(random.choice(coin_path))
coin.surr.y=-128
coin_mask = pygame.mask.from_surface(coin.img)
c=1
mixer.music.load("Teriyaki Boyz - Tokyo Drift Instrumental [ 1 Hour ].mp3")
mixer.music.play()

while run:

    win.blit(back_end, (0, 0))
    win.blit(wrong,(125,100))
    win.blit(racing,(240,225))
    win.blit(press,(185,400))
    srt=pygame.key.get_pressed()
    if(srt[pygame.K_SPACE]):
        starter=1
    if(starter==1):
        if (player_mask.overlap(dis_mask, (disturbance.surr.x - player.surr.x, disturbance.surr.y - player.surr.y))):
            win.blit(back_end, (0, 0))
            win.blit(game_over,(150,150))
            win.blit(final_score,(300,300))
            overall=0
        if(overall):
            inp=pygame.key.get_pressed()

            win.blit(back,(0,bgY))
            win.blit(back,(0,bgY-650))

            bgY+=velocity
            if velocity<maxspeed:
                velocity+=acceleration
            if bgY>=649.9:
                bgY=0

            player.move(inp)

            disturbance.move(0)


            if(disturbance.surr.y>860):
                disturbance = Vehicle()
                disturbance.surr.y=-128
                disturbance.surr.x=(random.choice(x_path))
                i+=1
            if(disturbance.surr.y>850):
                flag=1
            if(flag == 1 ):
                coin.move()
                if(player_mask.overlap(coin_mask,(coin.surr.x-player.surr.x,coin.surr.y-player.surr.y))):
                    score+=1
                    coin.surr.y=-128
                    coin.surr.x=(random.choice(coin_path))

                if(coin.surr.y>860):
                    coin.surr.y=-128
                    coin.surr.x=(random.choice(coin_path))

            print(score)
            score_text = font.render(f'Score : {score}', True, (255,255,255))
            final_score = font.render(f'Your score is : {score}',True,(0,0,0))
            win.blit(score_text, (50, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    pygame.display.update()