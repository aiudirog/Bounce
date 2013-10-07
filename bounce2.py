import sys, pygame, random, os, platform, time, math
from pygame.locals import *
from ball_class import *
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
                
def exit_now():
    sys.exit()
    pygame.quit()
                


def mov_poke_into_ball(mon_shrunk, mon_rect, mon_size, current_death_star_pokeball, catchball_rect, catchball_size):
    ball = current_death_star_pokeball
    ball_rect = catchball_rect
    ball_size = catchball_size
    mon = mon_shrunk
    # Formula for movement:
    #  x = x, + vt + 1/2at ** 2
    #  v = (1/2a t**2) / t
    #  v = (1/2a x**2) / x
    #acceleration:
    if is_mac == True:
        a = 0.002
    else:
        a = 0.003
    #final horizontal point:
    x = (ball_rect.right-mon_rect.right/1.25)# - (ball_size[0] / 1))
    if (x%2) != 0:
        x += 1
    v = (-(a/2 * (x**2)))/x
    
    counter = 0
    scaler = 1.0
    vert_old = 0
    while mon_rect.top <= (ball_rect.bottom - (ball_size[1] / 1.8)):
        to_exit_or_not_to_exit()
        vert = int(v*(counter) + a/2*(counter**2))
        vert_dif = vert - vert_old
        x_scaled = int(mon_size[0] / scaler)
        y_scaled = int(mon_size[1] / scaler)
        mon_shrunk = pygame.transform.smoothscale(mon, (x_scaled, y_scaled))
        #mon_rect = mon_shrunk.get_rect()
        mon_rect = mon_rect.move(2, vert_dif)
        #mon_rect.right += 2
        #mon_rect.top += vert_dif
        print counter, "|", vert, "|", v, "|", x
        screen.fill(background)
        screen.blit(ball, ball_rect)
        screen.blit(mon_shrunk, mon_rect)
        pygame.display.flip()
        counter += 2
        vert_old = vert
#Eventually need to make scaler run proportional to x so that it is a smooth scale down to 10% over the arc.
        if scaler  < 50:
            scaler += 0.01
    values_that_need_to_be_returned = [mon_shrunk, mon_rect]
    return (values_that_need_to_be_returned)
            
first_time = True
my_path = module_path()
dir = my_path
image_list = []
file_names = []
balls = []
list_of_death_star_pokeballs = []
death_star_pokeballs = []
            

    
is_mac = False
if os.name == "posix":
    plat = platform.system() 
    if plat == "Darwin":
        speed_list = [5,25]
        is_mac = True
    else:
        speed_list = [2,10]
else:
    speed_list = [2,10]
        

           
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

background = 255, 255, 255
        
               
    #Create a list of all images in dir.balls.
for files in os.listdir("Balls"):
    if files.endswith(".png"):
        image_list.append(files)

        
for image in image_list:
    ball = Ball(image, random.randint(*speed_list), random.randint(*speed_list), screen)
    balls.append(ball)   
    
while True:
    stored_second = 61
    Timer = random.randint(5,10)   
     
    while Timer > 0:
        to_exit_or_not_to_exit()
        
        screen.fill(background)
        
        for ball in balls:
            ball.update()
            ball.render()
            
        pygame.display.flip()
        current_second = time.localtime()[5]
        if stored_second != current_second:
            stored_second = current_second
            Timer -= 1
      
    Timer = 4
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
            
    catchball = pygame.image.load("0000.png")
    catchball_size = catchball.get_size()
    #catchball = pygame.transform.smoothscale(catchball, (catchball_size[0] / 3, catchball_size[1] / 3))
    #catchball_size = catchball.get_size()
    catchball_rect = catchball.get_rect()
    
    if first_time == True:
        first_time = False
        for files in os.listdir(os.path.join("Premium_Ball" , "output", "no_shadows_resized")):
            if files.endswith(".png"):
                list_of_death_star_pokeballs.append(files)
                
        list_of_death_star_pokeballs.sort()
        loaded_death_star_pokeballs = []
        front_face_loaded_death_star_pokeballs = []


        for index, image in enumerate(list_of_death_star_pokeballs):
            to_exit_or_not_to_exit()
            loaded_death_star_pokeballs.append(pygame.image.load(os.path.join(dir, "Premium_Ball" , "output", "no_shadows_resized", image)))
            front_face_loaded_death_star_pokeballs.append(pygame.image.load(os.path.join(dir, "Premium_Ball" , "output", "Slice_resized", image)))
            #loaded_death_star_pokeballs[index] = pygame.transform.smoothscale(loaded_death_star_pokeballs[index], (catchball_size[0], catchball_size[1]))
            #front_face_loaded_death_star_pokeballs[index] = pygame.transform.smoothscale(front_face_loaded_death_star_pokeballs[index], (catchball_size[0], catchball_size[1]))
            front_face_loaded_death_star_pokeballs.sort()
            loaded_death_star_pokeballs.sort()

    else:
        front_face_loaded_death_star_pokeballs.reverse()
        loaded_death_star_pokeballs.reverse()
        
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


    for index, image in enumerate(loaded_death_star_pokeballs):
        to_exit_or_not_to_exit()
        screen.fill(background)
        screen.blit(mon_shrunk, mon_rect)
        screen.blit(image, catchball_rect)
        pygame.display.flip()
        end_frame = index    

    new_mon = mov_poke_into_ball(mon_shrunk, mon_rect, mon_size, loaded_death_star_pokeballs[end_frame], catchball_rect, catchball_size)
    mon_shrunk = new_mon[0]
    mon_rect = new_mon[1]
    front_face_loaded_death_star_pokeballs.reverse()
    loaded_death_star_pokeballs.reverse()

    for index, image in enumerate(loaded_death_star_pokeballs):
        to_exit_or_not_to_exit()
        screen.fill(background)
        screen.blit(image, catchball_rect)
        screen.blit(mon_shrunk, mon_rect)
        screen.blit(front_face_loaded_death_star_pokeballs[index], catchball_rect)
        pygame.display.flip()
        
    screen.blit(catchball, catchball_rect)
    pygame.display.flip()

    catchball_speed = [-1,6]

    for num in range(100000):
        to_exit_or_not_to_exit()
    while True:
        to_exit_or_not_to_exit()
        catchball_rect = catchball_rect.move(catchball_speed)
        mon_rect = mon_rect.move(mon_speed)
        if catchball_rect.top > HEIGHT:
            break
        screen.fill(background)
        screen.blit(catchball, catchball_rect)
        pygame.display.flip()
        
    for num in range(100000):
        to_exit_or_not_to_exit()