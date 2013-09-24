import sys, pygame, random, os
from pygame.locals import *
pygame.init()


ballrect = []
dimmension = []
image_list = []
file_names = []
x_speed = []
y_speed = []

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

background = 255, 255, 255

def will_be_off_screen(dimmensions):
    if dimmensions.left < 0:
        return(1)
    elif dimmensions.right > WIDTH:
        return(2)
    elif dimmensions.top < 0:
        return(3)
    elif dimmensions.bottom > HEIGHT:
        return(4)
    else:
        return(0)

#Create a list of all images in dir.balls.
for files in os.listdir("Balls"):
    if files.endswith(".png"):
        image_list.append(files)

#Load all images.
count = 0
for image in image_list:
    dir = os.path.dirname(__file__)
    file_names.append(pygame.image.load(os.path.join(dir, "Balls" , image_list[count])))
    x_speed.append(random.randint(1,10))
    y_speed.append(random.randint(1,10))
    count += 1

x = 2

#prepare dimmesions and speed of balls.
a = 0
for ball in file_names:
    ballrect.append(ball.get_rect())
    dimmension.append(ballrect[a].move(x_speed[a], y_speed[a]))
    a += 1

i = 0


n = 0 #Frame Counter:

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                    
    for ball in file_names:

        #dimmension[i] = ballrect[i].move(x_speed[i], y_speed[i])
        dimmension[i] = dimmension[i].move(x_speed[i], y_speed[i])
        
#Change direction and speed when encountering a wall.
#This works. I know that.--------------------------
        if dimmension[i].left < 0 and dimmension[i].top < 0:
            x_speed[i] = -x_speed[i]
            y_speed[i] = -y_speed[i]
        elif dimmension[i].left < 0 and dimmension[i].bottom > HEIGHT:
            x_speed[i] = -x_speed[i]
            y_speed[i] = -y_speed[i]
        elif dimmension[i].right > WIDTH  and dimmension[i].top < 0:
            x_speed[i] = -x_speed[i]
            y_speed[i] = -y_speed[i]
        elif dimmension[i].right > WIDTH and dimmension[i].bottom > HEIGHT:
            x_speed[i] = -x_speed[i]
            y_speed[i] = -y_speed[i]
        elif dimmension[i].left < 0 or dimmension[i].right > WIDTH:
            if x_speed[i] < 0:
                x_speed[i] = random.randint(1,10)
            else:
                x_speed[i] = random.randint(1,10)
                x_speed[i] = -x_speed[i]
            if y_speed[i] < 0:
                y_speed[i] = random.randint(1,10)
                y_speed[i] = -y_speed[i]
            else:
                y_speed[i] = random.randint(1,10)

        elif dimmension[i].top < 0 or dimmension[i].bottom > HEIGHT:
            if y_speed[i] < 0:
                y_speed[i] = random.randint(1,10)
            else:
                y_speed[i] = random.randint(1,10)
                y_speed[i] = -y_speed[i]
            if x_speed[i] < 0:
                x_speed[i] = random.randint(1,10)
                x_speed[i] = -x_speed[i]
            else:
                x_speed[i] = random.randint(1,10)
        for z in range(4):
            off = will_be_off_screen(dimmension[i])
            if off != 0:
                if off == 1:
                    dimmension[i].left = 0
                if off == 2:
                    dimmension[i].right = WIDTH
                if off == 3:
                    dimmension[i].top = 0
                if off == 4:
                    dimmension[i].bottom = HEIGHT
#---------------------------------------------------

    #Used to force speed change:        
        #x_speed[i] += 2
        #y_speed[i] += 2

        i += 1
    i = 0
    screen.fill(background)
    for ball in file_names:
        screen.blit(file_names[i], dimmension[i])
        i += 1
    pygame.display.flip()

#Debugging output:
#-------------------
    #print i
    #print n
    #print x_speed
    #print y_speed
    #print ballrect[i]
    #print dimmension[i]
    #print file_names
    #n += 1
#--------------------
    i = 0

    
    
