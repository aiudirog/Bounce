import sys, pygame, random, os, platform
from pygame.locals import *
import pygame._view
pygame.init()

def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(unicode(sys.executable, encoding))
    return os.path.dirname(unicode(__file__, encoding))
    
my_path = module_path()

ballrect = []
dimmension = []
image_list = []
file_names = []
x_speed = []
y_speed = []
speed_list = []

if os.name == "posix":
    plat = platform.system() 
    if plat == "Darwin":
        speed_list = [5,25]
else:
    speed_list = [2,10]
    
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
    dir = my_path #os.path.dirname(__file__)
    file_names.append(pygame.image.load(os.path.join(dir, "Balls" , image_list[count])))
    x_speed.append(random.randint(*speed_list))
    y_speed.append(random.randint(*speed_list))
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

while n < 200:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                    
    for ball in file_names:

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
                x_speed[i] = random.randint(*speed_list)
            else:
                x_speed[i] = random.randint(*speed_list)
                x_speed[i] = -x_speed[i]
            if y_speed[i] < 0:
                y_speed[i] = random.randint(*speed_list)
                y_speed[i] = -y_speed[i]
            else:
                y_speed[i] = random.randint(*speed_list)

        elif dimmension[i].top < 0 or dimmension[i].bottom > HEIGHT:
            if y_speed[i] < 0:
                y_speed[i] = random.randint(*speed_list)
            else:
                y_speed[i] = random.randint(*speed_list)
                y_speed[i] = -y_speed[i]
            if x_speed[i] < 0:
                x_speed[i] = random.randint(*speed_list)
                x_speed[i] = -x_speed[i]
            else:
                x_speed[i] = random.randint(*speed_list)
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
        i += 1
    i = 0
    screen.fill(background)
    for ball in file_names:
        screen.blit(file_names[i], dimmension[i])
        i += 1
    pygame.display.flip()
    n += 1
    
    #Debugging output:
#-------------------
    #print i
    print n
    #print x_speed
    #print y_speed
    #print ballrect[i]
    #print dimmension[i]
    #print file_names
    #n += 1
#--------------------
    i = 0
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                    
    for ball in file_names:

        dimmension[i] = dimmension[i].move(x_speed[i], y_speed[i])
        i += 1
    i = 0
    screen.fill(background)
    for ball in file_names:
        screen.blit(file_names[i], dimmension[i])
        i += 1
    i = 0
    pygame.display.flip()
    n += 0



    
    
