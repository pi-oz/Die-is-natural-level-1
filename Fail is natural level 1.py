import pygame
import time
pygame.init()
screen=pygame.display.set_mode((800,600))
# color
black=(0,0,0)
white=(255,255,255)
purple=(125,0,125)
# character position
head_x,head_y=50,450
chest_x,chest_y=46,460
left_leg_x,left_leg_y=49,480
right_leg_x,right_leg_y=57,480
# Movement
left_right=5
leg_movement=1
# jump physics
gravity=0.8
jump_power=-18
y_velocity=0
onground=True
velocity=3
# floor
xfloor=800
refloor_con=False
# Text
font=pygame.font.SysFont("None",48)
run=True
clock=pygame.time.Clock()
# draw character
def character():
    head=pygame.draw.rect(screen,black,(head_x,head_y,10,10))
    chest=pygame.draw.rect(screen,black,(chest_x,chest_y,18,20))
    left_leg=pygame.draw.rect(screen,black,(left_leg_x,left_leg_y,3,20))
    right_leg=pygame.draw.rect(screen,black,(right_leg_x,right_leg_y,3,20))
    right_circle=pygame.draw.circle(screen,black,(right_leg_x+1,right_leg_y+17),5)
    left_circle=pygame.draw.circle(screen,black,(left_leg_x+1,left_leg_y+17),5)
# gravity+jump
def grav():
    global head_y, chest_y, left_leg_y, right_leg_y,y_velocity,onground
    y_velocity+=gravity
    head_y+=y_velocity
    chest_y+=y_velocity
    left_leg_y+=(y_velocity-leg_movement)
    right_leg_y+=(y_velocity-leg_movement)
    if left_leg_x<400 or right_leg_x>450:
        if right_leg_y>=480:
            right_leg_y=480
            left_leg_y=480
            head_y=450
            chest_y=460
            onground=True
# for smooth shrink texture floor
def xfloo():
    global xfloor
    if xfloor > 400:
        xfloor -= 40
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            run=False 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                run=False 
            if right_leg_x<400 or right_leg_x>450:
                if event.key==pygame.K_UP and onground:
                    y_velocity=jump_power    
                    onground=False
                    
    press=pygame.key.get_pressed()
    # right movement
    if press[pygame.K_RIGHT]:
        head_x+=left_right
        chest_x+=left_right
        left_leg_x+=left_right
        right_leg_x+=left_right
    # left movement  
    if press[pygame.K_LEFT]:
        head_x-=left_right
        chest_x-=left_right
        left_leg_x-=left_right
        right_leg_x-=left_right
    if right_leg_x>=700:
        text=font.render("You win!!!",True,black)
        screen.blit(text,(300,400))
    if right_leg_x>=750:
        run=False
    # x,y=pygame.mouse.get_pos()
    # print(x,y)
    grav()
    if right_leg_x>350:
        xfloo()
        refloor_con=True
    if  refloor_con:
        refloor=pygame.draw.rect(screen,purple,(450,500,350,100))
    if right_leg_y>510:
        run=False
    floor=pygame.draw.rect(screen,purple,(0,500,xfloor,100))
    character()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
        