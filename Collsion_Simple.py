#Simple Collision Detection Game
import random
import pygame
import sys
import time
#X and Y contain size of Window
X=800
Y=600
flag=True   #Flag for while
#a,b,c,d are coordinate of the first rectangle
a=400
b=400
c=40
d=40
#a1,b1 coordinates of second rectangle
a1=200
b1=200

pygame.init()
screen=pygame.display.set_mode((X,Y))
pygame.draw.rect(screen, (255,0,0),(a,b, c,d),0)
font=pygame.font.SysFont('Times New Roman', 15)
font1=pygame.font.SysFont('Times New Roman', 30)
pygame.draw.rect(screen, (255,255,0),(a1,b1,50,50),0)
pygame.display.set_caption("Catch")
text = font1.render("Catch the Yellow Rectangle", True, (255, 255, 255))    
screen.blit(text, (50,150))
pygame.display.update()
time.sleep(1)
#when Keyboard response is required.
def pressed():
    global a
    global b
    velocity=random.randint(0,10)
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        a=a-velocity
        screen.fill((0,0,0))
        if a>0 :
            pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)
        else:  
             a=800     
             pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)   
        
    elif key[pygame.K_RIGHT]:
        a=a+velocity
        screen.fill((0,0,0))
        if a<800 :
            pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)
        else:  
             a=0     
             pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)   
        
    elif key[pygame.K_UP]:
        b=b-velocity
        screen.fill((0,0,0))
        if b>0 :
            pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)
        else:  
             b=600     
             pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)   
          
    elif key[pygame.K_DOWN]:
        b=b+velocity
        screen.fill((0,0,0))
        if b<600 :
            pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)
        else:  
             b=0     
             pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)   
                                 
    else:
         pygame.draw.rect(screen, (255,0,0),(a,b,c,d),0)     
    pygame.display.update()
    
#randomise the movement of the enemy rectangle        
def enemy():
        p=random.randint(0,1)
        x1=random.randint(0,10)
        v=random.randint(0,10)
        k=random.randint(-5,5)
        k2=random.randint(-5,5)
        global a1
        global b1
        if p!=1:
                a1=a1+x1*k
                b1=b1+v*k2
        if a1>750:
                  a1=a1-750*x1
        elif b1>550:
                  b1=b1-550*v
        elif a1<0:
                a1=a1+750*x1
        elif b1<0:
                b1=-b1+550*v                
        screen.fill((0,0,0))        
        pygame.draw.rect(screen, (255,255,0),(a1,b1,50,50),0)
         
def match():
            global a
            global b
            global a1
            global b1
            global flag
            global font1
            if a1>a and a+c>a1 and b1>b and b+d>b1:    #if the enemy rectangle coordinates touch our rectangle coordinates you win
                text = font1.render("You Win", True, (255, 255, 255))
                screen.blit(text, (50, 150))
                pygame.display.update()
                time.sleep(1)
                print("You Win")
                flag=False

#To exit at any time                    
def exit(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global sorting
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)
        if click[0] == 1:
            pygame.quit() 
    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)
    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, (x + 10, y + 10))


while flag:
           exit("EXIT",20,20,60,40)
           pygame.display.update()
           pressed()
           enemy()
           match()
           for event in pygame.event.get():
            if(event.type==pygame.QUIT):
             pygame.quit()
             sys.exit()
           
             
