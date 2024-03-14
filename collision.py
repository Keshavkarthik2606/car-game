import pygame
win=pygame.display.set_mode((1000,500))
run=1
# class car:
#     def __init__(self):
#         self.rc=pygame.transform.scale(pygame.image.load("Black_viper.png"),(128,128))
#         self.surr = self.rc.get_rect()
#     def move(self):
#         win.blit(self.rc,(self.surr,0))
#         # if inp[pygame.K_LEFT] and self.surr>150:
#         #     self.surr-=5
#         # elif inp[pygame.K_RIGHT] and self.surr<575:
#         #     self.surr+=5
x=250
y=250

car=pygame.transform.scale(pygame.image.load("Black_viper.png"),(128,128))
car_surr=car.get_rect()
car_surr.x=0
car_surr.y=250
car_mask=pygame.mask.from_surface(car)

lorry=pygame.transform.scale(pygame.image.load("taxi.png"),(128,128))
lorry_surr=lorry.get_rect()
lorry_surr.x=600
lorry_surr.y=250
lorry_mask=pygame.mask.from_surface(lorry)



while run:

    pygame.display.update()
    inp=pygame.key.get_pressed()

    win.blit(lorry,(lorry_surr))

    if(inp[pygame.K_LEFT]):
        car_surr.x -= 1
    if (inp[pygame.K_RIGHT]):
        car_surr.x += 1

    win.blit(car, (car_surr))

    if(car_mask.overlap(lorry_mask,(lorry_surr.x-car_surr.x,lorry_surr.y-car_surr.y))):
        run=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0

    pygame.time.delay(10)