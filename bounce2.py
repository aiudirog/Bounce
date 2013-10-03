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
def mov_poke_into_ball(mon_shrunk, mon_rect, current_death_star_pokeball, catchball_rect, catchball_size):
    ball = current_death_star_pokeball
    ball_rect = catchball_rect
    ball_size = catchball_size

    # Formula for movement:
    #  x = x, + vt + 1/2at ** 2
    #  v = (1/2a t**2) / t
    #  v = (1/2a x**2) / x
    #acceleration:
    a = 32
    #final horisontal point:
    x = ball_rect.right - (ball_size[0] / 3)
    if (x%2) != 0:
        x += 1
    v = a/2 * (x**2)
    counter = 0
    for num in range(x/2):
        vert = v(counter) + a/2(counter**2)
        mon_rect = mon_rect.move(counter, vert)

    
    
    
if os.name == "posix":
    plat = platform.system() 
    if plat == "Darwin":
        speed_list = [5,25]
    else:
        speed_list = [2,10]
else:
    speed_list = [2,10]
        
image_list = []
file_names = []
balls = []
list_of_death_star_pokeballs = []
death_star_pokeballs = []
           
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

background = 255, 255, 255
my_path = module_path()               
               
    #Create a list of all images in dir.balls.
for files in os.listdir("Balls"):
    if files.endswith(".png"):
        image_list.append(files)

dir = my_path
    
class Ball():

    def __init__(self, image, x, y): 
    #This function runs when you create the class.
        self.speed = [x,y]
        self.image = image
        self.ball = None
        self.ballrect = None
        
        self.setup()
    
    def setup(self):
        self.ball = pygame.image.load(os.path.join(dir, "Balls" , self.image))
        self.ballrect = self.ball.get_rect()
        
    def update(self):
    #Change direction and speed when encountering a wall.
    #This works. I know that.--------------------------
        self.ballrect = self.ballrect.move(self.speed)
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
            if self.speed[1] < 0:
                self.speed[1] = random.randint(*speed_list)
                self.speed[1] = -self.speed[1]
            else:
                self.speed[1] = random.randint(*speed_list)

        elif self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            if self.speed[1] < 0:
                self.speed[1] = random.randint(*speed_list)
            else:
                self.speed[1] = random.randint(*speed_list)
                self.speed[1] = -self.speed[1]
            if self.speed[0] < 0:
                self.speed[0] = random.randint(*speed_list)
                self.speed[0] = -self.speed[0]
            else:
                self.speed[0] = random.randint(*speed_list)
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
    def update_no_boundaries(self):    
        self.ballrect = self.ballrect.move(self.speed)
    
    def render(self, screen):
        screen.blit(self.ball, self.ballrect)            
               
for image in image_list:
    ball = Ball(image, random.randint(*speed_list), random.randint(*speed_list))
    balls.append(ball)   

stored_second = 61
Timer = random.randint(5,10)   
 
while Timer > 0:
    to_exit_or_not_to_exit()
    
    screen.fill(background)
    
    for ball in balls:
        ball.update()
        ball.render(screen)
        
    pygame.display.flip()
    current_second = time.localtime()[5]
    if stored_second != current_second:
        stored_second = current_second
        Timer -= 1
  
Timer = 8
while Timer > 0:
    to_exit_or_not_to_exit()
    
    screen.fill(background)
    
    for ball in balls:
        ball.update_no_boundaries()
        ball.render(screen)
        
    pygame.display.flip()
    current_second = time.localtime()[5]
    if stored_second != current_second:
        stored_second = current_second
        Timer -= 1





  
mon = pygame.image.load("600px-001Bulbasaur.png")
scale = 100
for r in range(100):

    to_exit_or_not_to_exit()
    mon_size = mon.get_size()
    mon_shrunk = pygame.transform.smoothscale(mon, (mon_size[0] / scale, mon_size[1] / scale))
    mon_size = mon_shrunk.get_size()
    mon_rect = mon_shrunk.get_rect()
    mon_rect.left = (WIDTH/2 - mon_size[0]/2)
    mon_rect.top = (HEIGHT/2 - mon_size[1]/2)
    screen.fill(background)
    screen.blit(mon_shrunk, mon_rect)
    pygame.display.flip()
    scale -= 1
    
    
catchball = pygame.image.load("0000.png")
catchball_size = catchball.get_size()
catchball = pygame.transform.smoothscale(catchball, (catchball_size[0] / 3, catchball_size[1] / 3))
catchball_size = catchball.get_size()
catchball_rect = catchball.get_rect()

catchball_rect.left = WIDTH
catchball_rect.bottom = (HEIGHT/2)
screen.fill(background)
screen.blit(mon_shrunk, mon_rect)
screen.fill(background)
screen.blit(mon_shrunk, mon_rect)
screen.blit(catchball, catchball_rect)
pygame.display.flip()
catchball_speed = [-6,6]
touched_bottom = False
#move ball across screen and bounce on bottom.
mon_speed = [-6,0]
while True:
    to_exit_or_not_to_exit()
    catchball_rect = catchball_rect.move(catchball_speed)
    if catchball_rect.bottom > HEIGHT:
        catchball_speed [1] = -catchball_speed[1]
        touched_bottom = True
    if touched_bottom == True:
        if catchball_rect.bottom < (HEIGHT/2 + catchball_size[1]/3):
            break
    mon_rect = mon_rect.move(mon_speed)
    if mon_rect.left < 0:
        mon_speed = [0,0]
    screen.fill(background)
    screen.blit(mon_shrunk, mon_rect)
    screen.blit(catchball, catchball_rect)
    pygame.display.flip()

    
#Open Pokeball:
for files in os.listdir(os.path.join("Premium_Ball" , "output", "no_shadows")):
    if files.endswith(".png"):
        list_of_death_star_pokeballs.append(files)
        
for image in list_of_death_star_pokeballs:
    current_death_star_pokeball = pygame.image.load(os.path.join(dir, "Premium_Ball" , "output", "no_shadows", image))
    current_death_star_pokeball = pygame.transform.smoothscale(current_death_star_pokeball, (catchball_size[0], catchball_size[1]))
    screen.fill(background)
    screen.blit(mon_shrunk, mon_rect)
    screen.blit(current_death_star_pokeball, catchball_rect)
    pygame.display.flip()


  
while True:
    to_exit_or_not_to_exit()
