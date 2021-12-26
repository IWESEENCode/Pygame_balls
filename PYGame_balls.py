import pygame
from pygame.draw import *
from random import randint

pygame.init()

# game colors
black = 0, 0, 0
white = 255, 255, 255
light_grey = 220, 220, 220
grey = 192, 192, 192
dark_grey = 60, 60, 60
red = 255, 0, 0
purple = 160, 35, 255
pink = 255, 96, 208
light_green = 96, 255, 128
green = 0, 255, 0
light_blue = 80, 208, 255
blue = 0, 0, 255
yellow = 225, 225, 0
orange = 255, 160, 20
brown = 160, 130, 100

COLORS = [black, white, red, purple, pink, light_green,
          green, light_blue, blue, yellow, orange, brown]

# window setting
FPS = 60
win_x = 1000
win_y = 1000

screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("Шарики")

# game settings
score = 0
movespeed_x = 3
movespeed_y = 3

finished = False
need_click = False

clock = pygame.time.Clock()

# main defines
def draw_ball():
    global ball_x, ball_y, ball_r, color
    ball_r = randint(30, 80)
    ball_x = randint(0 + ball_r + 10, win_x - ball_r)
    ball_y = randint(0 + ball_r + 10, win_y - ball_r)
    color = COLORS[randint(0, 5)]

    circle(screen, color, (ball_x, ball_y), ball_r)

def click(event):
    """Проверяет попал ли игрок мышкой по фигуре на экране"""
    global score
    if (event.pos[1] - ball_y)**2 + (event.pos[0] - ball_x)**2 <= ball_r**2:
        score += 10
        print("попал, твои очки:", score)
    else:
        print("мимо, твои очки:", score)

def player_scores():
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Your score:", 1, yellow)
    text2 = f1.render(str(score), 1, yellow)

    screen.blit(text1, (10, 50))
    screen.blit(text2, (150, 50))

# TODO: need to create a class ball and add him opportunity
# to rebound out of themselves

# main loop
while not finished:
    clock.tick(FPS)
    
    if need_click == False:
        screen.fill((dark_grey))
        draw_ball()
        draw_ball()
        draw_ball()
        need_click = True

    if need_click:
        ball_x += movespeed_x
        ball_y += movespeed_y
        if ball_x - ball_r - 0 <= 10:
            movespeed_x *= -1
        if ball_y - ball_r - 0 <= 10:
            movespeed_y *= -1
        if ball_x + ball_r + 10 >= win_x:
            movespeed_x *= -1
        if ball_y + ball_r + 10 >= win_y:
            movespeed_y *= -1
    
    screen.fill((dark_grey))
    player_scores()
    circle(screen, color, (ball_x, ball_y), ball_r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            need_click = False
        
    pygame.display.update()
                 
pygame.quit()