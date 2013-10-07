import sys, pygame, random, os, platform, time
from pygame.locals import *

balls = []
images = ["0000.png", "0000.png", "0000.png", "0000.png"]
black = 0, 0, 0

size = WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode(size)



def to_exit_or_not_to_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                
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
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]
        
    def render(self, screen):
        screen.blit(self.ball, self.ballrect)


for image in images:
    ball = Ball(image, random.randint(5,20), random.randint(5,20))
    balls.append(ball)
    
while True:
    to_exit_or_not_to_exit()
    
    screen.fill(black)
    
    for ball in balls:
        ball.update()
        ball.render(screen)
    
    pygame.display.flip()