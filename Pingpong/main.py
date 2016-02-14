import pygame,random,sys
from pygame.locals import *

i=raw_input("How many AI do u want? (0,1 or 2):")

##Pygame init
pygame.init()

#VARIABLES init
FPS=60 ##FPS
fpsClock=pygame.time.Clock() #Object to set clock
disx=400 ##dimensions of
disy=600 ##the window.
disp=pygame.display.set_mode((disx,disy))##Window created
ball=pygame.image.load("data/ball.bmp")##Loading ball
board=pygame.image.load("data/board.bmp")##Loading board
board1=pygame.transform.flip(board,False,True)

ballx=(disx-20)/2##Ball's initial position, changed later on
bally=(disy-20)/2
ball_inr_x=0##Balls speed
ball_inr_y=0

##Only 3 colors :P
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

##Initialising boards
rectBoard1=pygame.Rect(0,50,100,10)
rectBoard2=pygame.Rect(disx-100,disy-5-50,100,10)

##Custon event handeler when user holds the key
## ## for second player
left_key_down=False
right_key_down=False
## ## for first player
a_key_down=False
d_key_down=False

#Points
player1_points=0
player2_points=0

#AI int the game
def AI1():
    global ballx,rectBoard1,d_key_down,a_key_down
    if(rectBoard1.centerx-20>ballx):
        d_key_down=False
        a_key_down=True
    elif(rectBoard1.centerx+20<ballx):
        a_key_down=False
        d_key_down=True
    else:
        a_key_down=False
        d_key_down=False
def AI2():
    global ballx,rectBoard2,left_key_down,right_key_down
    if(rectBoard2.centerx-20>ballx):
        right_key_down=False
        left_key_down=True
    elif(rectBoard2.centerx+20<ballx):
        left_key_down=False
        right_key_down=True
    else:
        left_key_down=False
        right_key_down=False

def AIU():
    global ballx,rectBoard1,d_key_down,a_key_down,ball_inr_x,ball_inr_y,bally
    temp_bally=bally
    temp_ballx=ballx
    temp_ball_inr_x=ball_inr_x
    temp_ball_inr_y=ball_inr_y
    if ball_inr_y<0 and temp_bally<disy/2:
        while not(temp_bally<50):
            temp_ballx=temp_ballx+temp_ball_inr_x;
            if(temp_ballx > disx-20):
                temp_ballx=disx-20
                temp_ball_inr_x=-temp_ball_inr_x
            if(temp_ballx < 0):
                temp_ballx=0
                temp_ball_inr_x=-temp_ball_inr_x

            temp_bally=temp_bally+temp_ball_inr_y;
    
    if(rectBoard1.centerx-30>temp_ballx+10):
        d_key_down=False
        a_key_down=True
    elif(rectBoard1.centerx+30<temp_ballx+10):
        a_key_down=False
        d_key_down=True
    else:
        a_key_down=False
        d_key_down=False
        

#reseting the ball
def ball_reset(player):
    global ballx,bally,ball_inr_x,ball_inr_y
    
    ballx=(disx-20)/2
    bally=(disy-20)/2
    ball_inr_x=random.randrange(-4,4)
    if ball_inr_x==0:
        ball_inr_x=random.randrange(1,4)
    ball_inr_y=random.randrange(3,6)
    #ball_inr_y=20

    ##switches the direction of the ball
    if player==-1:
        ball_inr_y=-ball_inr_y
    
##Ball initailized
ball_reset(1)

#pause condition
pause=False
##Exit condition
running=True


while running:
    ##Makes the background black
    disp.fill(black)

    #Checks all the events
    for event in pygame.event.get():

        #quit event
        if event.type==QUIT:
            running=False

        #Key down event
        elif event.type==KEYDOWN:
            #For second player
            if event.key==K_LEFT:
                left_key_down=True
            if event.key==K_RIGHT:
                right_key_down=True
                
            #For first player
            if event.key==K_a:
                a_key_down=True
            if event.key==K_d:
                d_key_down=True

            #For exit
            if event.key==K_ESCAPE:
                pause=not pause
                
        elif event.type==KEYUP:
            
            #For second player
            if event.key==K_LEFT:
                left_key_down=False
            if event.key==K_RIGHT:
                right_key_down=False
                
            #For first player
            if event.key==K_a:
                a_key_down=False
            if event.key==K_d:
                d_key_down=False


    ##Draws board1
    disp.blit(board1,rectBoard1)
    ##Draws board2
    disp.blit(board,rectBoard2)
    ##Draws ball
    disp.blit(ball,(ballx,bally))
    ##Draws mid line, for time pass
    pygame.draw.line(disp,white,(0,disy/2),(disx,disy/2),5)

    font=pygame.font.SysFont('Calibri',76,True,False)

    p1=font.render(str(player1_points),True,white)
    p2=font.render(str(player2_points),True,white)

    disp.blit(p1,(20,(disy/2)-76))
    disp.blit(p2,(20,(disy/2)+14))
    
    if(player2_points==10 or player1_points==10):
        running=False

    if pause==True:
        p1=font.render("PAUSED!",True,red)
        disp.blit(p1,(75,(disy/2)-30))
        
    else:
        ##If player 2 holds left/right key, board moves in respected direction
        if(left_key_down and rectBoard2.x>0):
            rectBoard2.x=rectBoard2.x-5    
        if(right_key_down and rectBoard2.x<disx-100):
            rectBoard2.x=rectBoard2.x+5

        
        if i=='1':
            AIU()
        elif i=='2': 
            AI2()
            AI1()
        elif i=='u':
            AIU()
            AI2()

        ##If player 1 holds A/D key, board moves in respected direction
        if(a_key_down and rectBoard1.x>0):
            rectBoard1.x=rectBoard1.x-5
        if(d_key_down and rectBoard1.x<disx-100):
            rectBoard1.x=rectBoard1.x+5

        #Velocity= ball_inr_x i+ball_inr_y j
        
        ballx=ballx+ball_inr_x;
        
        if(ballx > disx-20):
            ballx=disx-20
            ball_inr_x=-ball_inr_x
        if(ballx < 0):
            ballx=0
            ball_inr_x=-ball_inr_x

        bally=bally+ball_inr_y;
        
        ##Board 2 -below
        if(bally+20 > disy-50):#player 2 lost
            ball_reset(1)
            player1_points=player1_points+1
        elif(rectBoard2.colliderect((ballx,bally,20,20))):
            ball_inr_y=-ball_inr_y
            if(ballx+10<rectBoard2.x+30):
                ball_inr_x=ball_inr_x-2
            if(ballx+10>rectBoard2.x+70):
                ball_inr_x=ball_inr_x+2
            if(ballx+10<rectBoard2.x+10):
                ball_inr_x=ball_inr_x-4
            if(ballx+10>rectBoard2.x+90):
                ball_inr_x=ball_inr_x+4
                
        ##Board 1 -above
        if(bally < 50):##Player 1 lost
            ball_reset(-1)
            player2_points=player2_points+1
        elif(rectBoard1.colliderect((ballx,bally,20,20))):
            ball_inr_y=-ball_inr_y
            if(ballx+10<rectBoard1.x+30):
                ball_inr_x=ball_inr_x-2
            if(ballx+10>rectBoard1.x+70):
                ball_inr_x=ball_inr_x+2
            if(ballx+10<rectBoard1.x+10):
                ball_inr_x=ball_inr_x-4
            if(ballx+10>rectBoard1.x+90):
                ball_inr_x=ball_inr_x+4
    
    fpsClock.tick(FPS)
    pygame.display.update()

print "Player 1: " + str(player1_points) + "\n"
print "Player 2: " + str(player2_points) + "\n"


pygame.quit()
raw_input()

sys.exit()
