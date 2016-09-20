import pygame,sys,thread,random
from pygame.locals import *

pygame.init()
dispx=500
dispy=800
disp=pygame.display.set_mode((dispx,dispy))

FPS=30
fpsClock=pygame.time.Clock()
white=(129,152,241)
black=(255,255,255)
blue=(37,51,122)

check_inc_score1=False
collide_box1=0
check_inc_score2=False
collide_box2=0
SCORE=0
OLD_SCORE=0
SPEED=6
running=True
game_end=False
start_game=False
#Rectangles for lane 1
lane1_rect=(Rect(50,-50,50,50),
            Rect(50,-350,50,50),
            Rect(50,-650,50,50))
lane1_shape=[0,0,0]

collided_circle1=[False,False,False]

for rec in range(0,3):
    i=random.randint(0,10)
    if(i>=5):
        lane1_rect[rec].x=50
    elif(i<5):
        lane1_rect[rec].x=150
    i=random.randint(0,10)
    if(i>=5):
        lane1_shape[rec]=0
    elif(i<5):
        lane1_shape[rec]=1

#Rectangles for lane 2
lane2_rect=(Rect(300,-125,50,50),
            Rect(300,-425,50,50),
            Rect(300,-725,50,50))

lane2_shape=[0,0,0]

collided_circle2=[False,False,False]

for rec in range(0,3):
    i=random.randint(0,10)
    if(i>=5):
        lane2_rect[rec].x=300
    elif(i<5):
        lane2_rect[rec].x=400
    i=random.randint(0,10)
    if(i>=5):
        lane2_shape[rec]=0
    elif(i<5):
        lane2_shape[rec]=1

#lane 1 Car rect
car1_img=pygame.image.load("car_lane1.bmp")
lane1_car=Rect(50,650,50,75)
lane1_car_left=True

#lane 2 Car rect
car2_img=pygame.image.load("car_lane2.bmp")
lane2_car=Rect(300,650,50,75)
lane2_car_left=True

def inc_score_lane1():
    global check_inc_score1,lane1_rect,lane1_car,collide_box1,SCORE,SPEED

    if(not lane1_rect[collide_box1].colliderect(lane1_car)):
        if(check_inc_score1):
            SCORE+=1
            check_inc_score1=False
    
def inc_score_lane2():
    global check_inc_score2,lane2_rect,lane2_car,collide_box2,SCORE,SPEED

    if(not lane2_rect[collide_box2].colliderect(lane2_car)):
        if(check_inc_score2):
            SCORE+=1
            check_inc_score2=False

def draw_box(rectangle,shape,lane):
    global disp
    col=""
    if lane=="lane 1":
        col=(255,50,50)
    if lane=="lane 2":
        col=(150,100,255)
    if(shape==0):
        pygame.draw.rect(disp,col,rectangle,10)
    if(shape==1):
        pygame.draw.ellipse(disp,col,rectangle,10)
        
def lane1():
    global disp,lane1_rect,running,lane1_shape,collided_circle1,game_end
    
    for rec in range(0,3):
        if lane1_rect[rec].y>-50:
            if(lane1_shape[rec]==1):
                if(not collided_circle1[rec]):
                    draw_box(lane1_rect[rec],lane1_shape[rec],"lane 1")
            elif(lane1_shape[rec]==0):
                draw_box(lane1_rect[rec],lane1_shape[rec],"lane 1")

        if not game_end:
            lane1_rect[rec].y+=SPEED
            
            if lane1_shape[rec]==1:
                if ((lane1_rect[rec].y>(dispy-50)) and (not collided_circle1[rec])):
                    game_end=True
                if (lane1_rect[rec].y<(-50)):
                    collided_circle1[rec]=False
            if lane1_rect[rec].y>dispy:
                i=random.randint(0,10)
                if(i>=5):
                    lane1_rect[rec].x=50
                elif(i<5):
                    lane1_rect[rec].x=150
                i=random.randint(0,10)
                if(i>=5):
                    lane1_shape[rec]=0
                elif(i<5):
                    lane1_shape[rec]=1
                lane1_rect[rec].y=lane1_rect[rec-1].y-300

            
def car1():
    global disp,lane1_car,lane1_car_left
    if not game_end:
        if(lane1_car_left and lane1_car.x!=50):
            lane1_car.x-=25
        if(not lane1_car_left and lane1_car.x!=150):
            lane1_car.x+=25
    disp.blit(car1_img,lane1_car)
    collision_lane1()

def collision_lane1():
    global lane1_car,lane1_rect,lane1_shape,running,collide_box1,check_inc_score1,collided_circle1,game_end
    for i in range(0,3):
        if (lane1_car.colliderect(lane1_rect[i])):
            if lane1_shape[i]==0:
                game_end=True
            elif lane1_shape[i]==1:
                collide_box1=i
                collided_circle1[i]=True
                check_inc_score1=True
    
    inc_score_lane1()
    
def lane2():
    global disp,lane2_rect,running,lane2_shape,collided_circle2,game_end
    
    for rec in range(0,3):
        if lane2_rect[rec].y>-50:
            if(lane2_shape[rec]==1):
                if(not collided_circle2[rec]):
                    draw_box(lane2_rect[rec],lane2_shape[rec],"lane 2")
            elif(lane2_shape[rec]==0):
                draw_box(lane2_rect[rec],lane2_shape[rec],"lane 2")

        if not game_end:
            lane2_rect[rec].y+=SPEED

            if lane2_shape[rec]==1:
                if ((lane2_rect[rec].y>(dispy-50)) and (not collided_circle2[rec])):
                    game_end=True
                if (lane2_rect[rec].y<(-50)):
                    collided_circle2[rec]=False
                    
            if lane2_rect[rec].y>dispy:
                i=random.randint(0,10)
                if(i>=5):
                    lane2_rect[rec].x=300
                elif(i<5):
                    lane2_rect[rec].x=400
                i=random.randint(0,10)
                if(i>=5):
                    lane2_shape[rec]=0
                elif(i<5):
                    lane2_shape[rec]=1
                lane2_rect[rec].y=lane2_rect[rec-1].y-300

def car2():
    global disp,lane2_car,lane2_car_left
    if not game_end:
        if(lane2_car_left and lane2_car.x!=300):
            lane2_car.x-=25
        if(not lane2_car_left and lane2_car.x!=400):
            lane2_car.x+=25
    disp.blit(car2_img,lane2_car)
    collision_lane2()

def collision_lane2():
    global lane2_car,lane2_rect,lane2_shape,running,collide_box2,check_inc_score2,collided_circle2,game_end
    for i in range(0,3):
        if (lane2_car.colliderect(lane2_rect[i])):
            if lane2_shape[i]==0:
                game_end=True
            elif lane2_shape[i]==1:
                collide_box2=i
                collided_circle2[i]=True
                check_inc_score2=True
    inc_score_lane2()

def event_handling():
    global running,lane1_car_left,lane2_car_left,start_game
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==KEYDOWN:
            #first car events:
            if event.key==K_z:
                lane1_car_left= not lane1_car_left
            #second car events:
            if event.key==K_PERIOD:
                lane2_car_left= not lane2_car_left
            #start game:
            if event.key==K_SPACE:
                start_game=True
                

while running:
    event_handling()
    
    disp.fill(blue)
    font=pygame.font.SysFont('Calibri',76,True,False)

    pygame.draw.line(disp,white,(125,0),(125,dispy),2)
    pygame.draw.line(disp,white,(245,0),(245,dispy),10)
    pygame.draw.line(disp,white,(375,0),(375,dispy),2)

    if(start_game==True):
        lane1()
        lane2()
        car1()
        car2()
        
        if(not game_end):
            score_font=font.render(str(SCORE),True,black)
            disp.blit(score_font,(dispx/2-25,20))

        if(SCORE==OLD_SCORE+5):
            SPEED+=1
            OLD_SCORE=SCORE

        if game_end:

            game_end=font.render("Game ended",True,black)
            score_font=font.render("Score: "+str(SCORE),True,black)
            disp.blit(game_end,(50,(dispy/2)-76))
            disp.blit(score_font,(50,(dispy/2)+76))
    else:
        start1=font.render("Press space",True,black)
        start2=font.render("to start!",True,black)
        disp.blit(start1,(50,(dispy/2)-76))
        disp.blit(start2,(50,(dispy/2)+76))
        
    fpsClock.tick(FPS)
    pygame.display.update()


pygame.quit()
sys.exit()
