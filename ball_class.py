import sys, pygame, random, os, platform, time, math
from pygame.locals import *

def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(unicode(sys.executable, encoding))
    return os.path.dirname(unicode(__file__, encoding))

my_path = module_path()
dir = my_path

is_mac = False
if os.name == "posix":
    plat = platform.system() 
    if plat == "Darwin":
        is_mac = True
        

class Ball():
    
    def __init__(self, image, screen): 
    #This function runs when you create the class.
        self.speed = []
        self.image = image
        self.ball = None
        self.ballrect = None
        self.WIDTH = None
        self.HEIGHT = None
        self.speed_list = []
        self.screen = screen
        self.setup()
       
    def setup(self):
        self.ball = pygame.image.load(os.path.join(dir, "Balls" , self.image))
        self.ballrect = self.ball.get_rect()
        self.WIDTH, self.HEIGHT = self.screen.get_size()
        if is_mac == True:
            self.speed_list = [5,25]
        else:
            self.speed_list = [2,10]
        self.speed = [random.randint(*self.speed_list), random.randint(*self.speed_list)]
        
        
    def will_be_off_screen(self, dimmensions):
        if dimmensions.left < 0:
            return(1)
        elif dimmensions.right > self.WIDTH:
            return(2)
        elif dimmensions.top < 0:
            return(3)
        elif dimmensions.bottom > self.HEIGHT:
            return(4)
        else:
            return(0)    
            
    def update(self):
    #Change direction and speed when encountering a wall.
    #This works. I know that.--------------------------
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 and self.ballrect.top < 0:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.left < 0 and self.ballrect.bottom > self.HEIGHT:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.right > self.WIDTH  and self.ballrect.top < 0:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.right > self.WIDTH and self.ballrect.bottom > self.HEIGHT:
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
        elif self.ballrect.left < 0 or self.ballrect.right > self.WIDTH:
            if self.speed[0] < 0:
                self.speed[0] = random.randint(*self.speed_list)
            else:
                self.speed[0] = random.randint(*self.speed_list)
                self.speed[0] = -self.speed[0]
            if self.speed[1] < 0:
                self.speed[1] = random.randint(*self.speed_list)
                self.speed[1] = -self.speed[1]
            else:
                self.speed[1] = random.randint(*self.speed_list)

        elif self.ballrect.top < 0 or self.ballrect.bottom > self.HEIGHT:
            if self.speed[1] < 0:
                self.speed[1] = random.randint(*self.speed_list)
            else:
                self.speed[1] = random.randint(*self.speed_list)
                self.speed[1] = -self.speed[1]
            if self.speed[0] < 0:
                self.speed[0] = random.randint(*self.speed_list)
                self.speed[0] = -self.speed[0]
            else:
                self.speed[0] = random.randint(*self.speed_list)
        for z in range(4):
            off = self.will_be_off_screen(self.ballrect)
            if off != 0:
                if off == 1:
                    self.ballrect.left = 0
                if off == 2:
                    self.ballrect.right = self.WIDTH
                if off == 3:
                    self.ballrect.top = 0
                if off == 4:
                    self.ballrect.bottom = self.HEIGHT
                    
    def update_no_boundaries(self):    
        self.ballrect = self.ballrect.move(self.speed)
        
    def is_ball_off_the_screen_thingy_majig_edge_part_of_it(self):
        if self.ballrect.left > self.WIDTH:
            return True
        elif self.ballrect.top > self.HEIGHT:
            return True
        elif self.ballrect.right < 0:
            return True
        elif self.ballrect.bottom < 0:
            return True
        else:
            return False
    def render(self):
        self.screen.blit(self.ball, self.ballrect)    


