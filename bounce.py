import sys, pygame, random, os
from pygame.locals import *
pygame.init()

ballrect = []
dimmension = []
image_list = []

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

#x_speed = [2, 10, 2, 2, 2]
#y_speed = [2, 10, 2, 2, 2]
background = 255, 255, 255

#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

#ball = [pygame.image.load("ultraball.png"), ]

os.chdir("/balls")
for files in os.listdir("."):
    if files.endswith(".png"):
        image_list.append(files)

count = 0
for image in image_list:
   file_names.append(pygame.image.load(os.path.join("Balls" , image_list[count])))
   x_speed.append(2)
   y_speed.append(2)
   count += 1

x = 2
a = 0
for ball in file_names:
    ballrect.append(ball.get_rect())
    dimmension.append(ballrect[a].move(x_speed[a], y_speed[a]))
    a += 1

#for file in file_name:
    #load(file)
#ballrect = ball.get_rect()
i = 0
n = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                    
    for ball in file_names:
        #if i == x:
           #i = 0
        

        #dimmension[i] = ballrect[i].move(x_speed[i], y_speed[i])
        dimmension[i] = dimmension[i].move(x_speed[i], y_speed[i])
        
        if dimmension[i].left < 0 or dimmension[i].right > WIDTH:
            x_speed[i] = -x_speed[i]
            if y_speed[i] < 0:
                y_speed[i] = random.randint(1,20)
                y_speed[i] = -y_speed[i]
            else:
                y_speed[i] = random.randint(1,20)

        if dimmension[i].top < 0 or dimmension[i].bottom > HEIGHT:
            y_speed[i] = -y_speed[i]
            if x_speed[i] < 0:
                x_speed[i] = random.randint(1,20)
                x_speed[i] = -x_speed[i]
            else:
                x_speed[i] = random.randint(1,20)
                
        x_speed[i] += 2
        y_speed[i] += 2
        i += 1
    i = 0
    screen.fill(background)
    for ball in file_names:
        screen.blit(file_names[i], dimmension[i])
        i += 1
    pygame.display.flip()
    #print i
    print n
    print x_speed
    print y_speed
    #print ballrect[i]
    #print dimmension[i]
    print file_names
    i = 0
    n += 1
    
    
