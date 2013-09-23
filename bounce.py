import sys, pygame, random
from pygame.locals import *
pygame.init()

#image_list = {}

#def load(file_name):
    #if file_name in image_list:
        #return image_list[file_name]
    #image_list[file_name] = pygame.image.load(file_name)
    #return image_list[file_name]

#size = width, height =  1920, 1080
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
WIDTH, HEIGHT = screen.get_size() 

speed = [2,2]
black = 0, 0, 0

#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

#ball = [pygame.image.load("ultraball.png"), ]


file_name = {pygame.image.load("ultraball.png")}

#for file in file_name:
    #load(file)
#ballrect = ball.get_rect()

while 1:
    for ball in file_name:
        ballrect = ball.get_rect()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > WIDTH:
            speed[0] = -speed[0]
            if speed[1] < 0:
                speed[1] = random.randint(1,20)
                speed[1] = -speed[1]
            else:
                speed[1] = random.randint(1,20)

        if ballrect.top < 0 or ballrect.bottom > HEIGHT:
            speed[1] = -speed[1]
            if speed[0] < 0:
                speed[0] = random.randint(1,20)
                speed[0] = -speed[0]
            else:
                speed[0] = random.randint(1,20)
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    
