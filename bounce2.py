import sys, pygame, random, os, platform, time, math
from pygame.locals import *
from ball_class import *
from custom_functions import *
#import pygame._view
pygame.init()
            
first_time = True
my_path = module_path()
dir = my_path
image_list = []
file_names = []
balls = []
list_of_death_star_pokeballs = []
death_star_pokeballs = []
list_of_pokes = []
            

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

background = 255, 255, 255

def create_list_of_pokes():
    for files in os.listdir(os.path.join("pokes")):
        if files.endswith(".png"):
            list_of_pokes.append(files)
       
               
    #Create a list of all images in dir.balls.
for files in os.listdir("Balls"):
    if files.endswith(".png"):
        image_list.append(files)

    #Create a list of objects of type Balls.
for image in image_list:
    ball = Ball(image,  screen)
    balls.append(ball)   

create_list_of_pokes()
while True:
#--------------------------------------------------------------
#This first block is the random movement of balls
#on the screen.
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
 
#--------------------------------------------------------------
#This second block gives the balls a little bit of
#to leave the screen so that the next part can be
#loaded. 
    Timer = 5
    while Timer > 0:
        to_exit_or_not_to_exit()
        
        screen.fill(background)
        
        for ball in balls:
            ball.update_no_boundaries()
            ball.render()
           
        pygame.display.flip()
        current_second = time.localtime()[5]
        if stored_second != current_second:
            stored_second = current_second
            Timer -= 1


#--------------------------------------------------------------
#This next section of code prepares the pokemon
#and ball to enter the screen.            
    catchball = pygame.image.load("0000.png")
    catchball_size = catchball.get_size()
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
            front_face_loaded_death_star_pokeballs.sort()
            loaded_death_star_pokeballs.sort()

    else:
        front_face_loaded_death_star_pokeballs.reverse()
        loaded_death_star_pokeballs.reverse()

#--------------------------------------------------------------
#Load pokemon and ball to screen, then move
#them about.
    if len(list_of_pokes) == 0:
        create_list_of_pokes()
        
    number_of_pokes = len(list_of_pokes)
    random_poke = random.randint(0,(number_of_pokes-1))
    mon = pygame.image.load(os.path.join("pokes", list_of_pokes[random_poke])) 
    list_of_pokes.remove(list_of_pokes[random_poke])
        
    scale = 100
    for num in range(100):

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
    
#move ball across screen and bounce on bottom
    catchball_speed = [-6,6]
    touched_bottom = False
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
        if mon_rect.left < 6:
            mon_speed = [0,0]
        screen.fill(background)
        screen.blit(mon_shrunk, mon_rect)
        screen.blit(catchball, catchball_rect)
        pygame.display.flip()

#--------------------------------------------------------------
#Open Pokeball, move pokemon into it, close ball
    for index, image in enumerate(loaded_death_star_pokeballs):
        to_exit_or_not_to_exit()
        screen.fill(background)
        screen.blit(mon_shrunk, mon_rect)
        screen.blit(image, catchball_rect)
        pygame.display.flip()
        end_frame = index    

    new_mon = mov_poke_into_ball(mon_shrunk, mon_rect, mon_size, loaded_death_star_pokeballs[end_frame], catchball_rect, catchball_size, screen)
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
#--------------------------------------------------------------
#return to top