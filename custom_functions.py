import sys, pygame, random, os, platform, time, math
from pygame.locals import *

is_mac = False
if os.name == "posix":
    plat = platform.system() 
    if plat == "Darwin":
        is_mac = True
        
background = 255, 255, 255

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
                

def mov_poke_into_ball(mon_shrunk, mon_rect, mon_size, current_death_star_pokeball, catchball_rect, catchball_size, screen, front_face_loaded_death_star_pokeballs):
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
    x = (ball_rect.right-600/1.25)# - (ball_size[0] / 1))
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
        #mon_rect = mon_rect.move(2, vert_dif)
        mon_rect.right += 2
        mon_rect.top += vert_dif
        screen.fill(background)
        screen.blit(ball, ball_rect)
        screen.blit(mon_shrunk, mon_rect)
        screen.blit(front_face_loaded_death_star_pokeballs, ball_rect)
        pygame.display.flip()
        counter += 2
        vert_old = vert
        
        if scaler  < 50:
            scaler += 0.01
    values_that_need_to_be_returned = [mon_shrunk, mon_rect]
    return (values_that_need_to_be_returned)