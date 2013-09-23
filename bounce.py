import sys, pygame, random
from pygame.locals import *
pygame.init()

#image_list = {}
ballrect = []
dimmension = []
#def load(file_name):
    #if file_name in image_list:
        #return image_list[file_name]
    #image_list[file_name] = pygame.image.load(file_name)
    #return image_list[file_name]

#size = width, height =  1920, 1080
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

speed = [2,2]
black = 255, 0, 0

#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

#ball = [pygame.image.load("ultraball.png"), ]


file_names = [pygame.image.load("ultraball.png"), pygame.image.load("photo.jpg")]
x = 2
a = 0
for ball in file_names:
    ballrect.append(ball.get_rect())
    dimmension.append(ballrect[a].move(speed))
    a += 1

#for file in file_name:
    #load(file)
#ballrect = ball.get_rect()
i = 0
n = 0
while True:
    if i == x:
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        
    dimmension[i] = ballrect[i].move(speed)
    if dimmension[i].left < 0 or dimmension[i].right > WIDTH:
        speed[0] = -speed[0]
        if speed[1] < 0:
            speed[1] = random.randint(1,20)
            speed[1] = -speed[1]
        else:
            speed[1] = random.randint(1,20)

    if dimmension[i].top < 0 or dimmension[i].bottom > HEIGHT:
        speed[1] = -speed[1]
        if speed[0] < 0:
            speed[0] = random.randint(1,20)
            speed[0] = -speed[0]
        else:
            speed[0] = random.randint(1,20)

    screen.fill(black)
    screen.blit(file_names[i], dimmension[i])
    pygame.display.flip()
    print i
    print n
    print ballrect[i]
    print dimmension[i]
    print file_names
    i += 1
    n += 1
    
    
