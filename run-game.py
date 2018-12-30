import pygame
import time
pygame.init()

screenWidth = 500
screenHeight = 500
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Run-Game")
x = 50
y = 340
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 10
run =True

def redraw():
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x -vel> 0:
        x-= vel
    if keys[pygame.K_RIGHT] and x +vel + width < screenWidth:
        x+= vel
    if keys[pygame.K_SPACE]:
        isJump = True
    if isJump:
        if jumpCount >= -10:
            neg = 1
            if jumpCount <0:
                neg = -1
            y-= ((jumpCount) ** 2) /2 * neg
            jumpCount-=1

        else:
            isJump = False
            jumpCount = 10

    redraw()
