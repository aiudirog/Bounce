import sys, pygame, random, os, platform, time
from pygame.locals import *
#import pygame._view
pygame.init()

def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(unicode(sys.executable, encoding))
    return os.path.dirname(unicode(__file__, encoding))
        
def to_exit_or_not_to_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()

image_list = []
file_names = []
           
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

background = 255, 255, 255
my_path = module_path()               
               
    #Create a list of all images in dir.balls.
for files in os.listdir("Balls"):
    if files.endswith(".png"):
        image_list.append(files)
                  
class Ball():

    def __init__(self, image, x, y): 
    #This function runs when you create the class.
        self.speed = [x,y]
        self.image = image
        self.ball = None
        self.ballrect = None
        
        self.setup()
    
    def setup(self):
        self.ball = pygame.image.load(self.image)
        self.ballrect = self.ball.get_rect()
        
    def update(self):
    #Change direction and speed when encountering a wall.
    #This works. I know that.--------------------------
        if self.ballrect.left < 0 and self.ballrect.top < 0:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.left < 0 and self.ballrect.bottom > HEIGHT:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.right > WIDTH  and self.ballrect.top < 0:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.right > WIDTH and self.ballrect.bottom > HEIGHT:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.left < 0 or self.ballrect.right > WIDTH:
            if self.speed[0] < 0:
                self.speed[0] = random.randint(*speed_list)
            else:
                self.speed[0] = random.randint(*speed_list)
                self.speed[0] = -self.speed[0]
            if y_speed[i] < 0:
                y_speed[i] = random.randint(*speed_list)
                y_speed[i] = -y_speed[i]
            else:
                y_speed[i] = random.randint(*speed_list)

        elif self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            if y_speed[i] < 0:
                y_speed[i] = random.randint(*speed_list)
            else:
                y_speed[i] = random.randint(*speed_list)
                y_speed[i] = -y_speed[i]
            if x_speed[i] < 0:
                self.speed[0] = random.randint(*speed_list)
                self.speed[0] = -self.speed[0]
            else:
                x_speed[i] = random.randint(*speed_list)
        for z in range(4):
            off = will_be_off_screen(self.ballrect)
            if off != 0:
                if off == 1:
                    self.ballrect.left = 0
                if off == 2:
                    self.ballrect.right = WIDTH
                if off == 3:
                    self.ballrect.top = 0
                if off == 4:
                    self.ballrect.bottom = HEIGHT
        
    def render(self, screen):
        screen.blit(self.ball, self.ballrect)            
               
               
                
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