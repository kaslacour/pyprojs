import pygame
from numpy import min
from pygame import Vector2 as vec2
from numpy import array as arr
from numpy import clip, sign
from numpy.linalg import norm

CANVAS_WIDTH = float(400)
CANVAS_HEIGHT = float(400)

def RHS(t: float, Y: arr) -> arr:

    # d2x/dt2 = 0.01 * dx/dt
    # d2y/dt2 = -1

    # dx/dt = z
    # dz/dt = -1 * sign(z) * z^2
    # dy/dt = w
    # dw/dt = -1 - 1 * sign(w) * w^2

    x, dxdt, y, dydt = Y
    vel = norm([dxdt,dydt],2)
    drag = 0.2 * vel**2


    dYdt = arr([dxdt, -drag*dxdt/vel, dydt, -10-drag*dydt/vel])
    if Y[2] <= -0.5+1e-4:
        dYdt[1] -= 0.1*sign(dxdt)

    
    return dYdt

def integrateMotion(dt: float, t: float, Y: arr) -> arr:
    T = t
    timeLeft = dt
    timeStep = 0.0001
    timeStep = min([timeStep, timeLeft])
    Y_next = Y
    while timeLeft > 0.0:
        k1 = RHS(t, Y_next)
        k2 = RHS(t+timeStep/2, Y_next + timeStep * k1 / 2.0)
        k3 = RHS(t+timeStep/2, Y_next + timeStep * k2 / 2.0)
        k4 = RHS(t+timeStep, Y_next + timeStep * k3)
        t += timeStep
        Y_next += timeStep / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        if Y_next[0] > 0.5 or Y_next[0] < -0.5:
            Y_next[0] = clip(Y_next[0],-0.5,0.5)
            Y_next[1] = - 0.9*Y_next[1]
        if Y_next[2] < -0.5:
            Y_next[2] = clip(Y_next[2],-0.5,0.5)
            Y_next[3] = -0.9*Y_next[3]
        timeLeft -= timeStep
        timeStep = min([timeStep, timeLeft])
    return Y_next


pygame.init()
screen = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
t = 0
Y = arr([0.0, 5.0, 0.0, 4.0])
while running:
    # poll for events
    # pygame.QUIT means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    # fill the screen witha colour to wipe away anything from last frame
    screen.fill(pygame.Color(140,140,255))

    

    # RENDER GAME HERE
    coords = integrateMotion(dt,t,Y)

    game_coords = vec2(0.5 + Y[0], -0.5 + Y[2])
    game_coords.x *= CANVAS_WIDTH
    game_coords.y *= -CANVAS_HEIGHT


    pygame.draw.circle(screen,pygame.Color(255,127,0),game_coords,radius=10)

    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    '''


    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick() / 1000
    t += dt
    #print("Time passed: {0}".format(t))
    print("Frame rate: ",clock.get_fps())

pygame.quit()