from pygame import *
from random import randint
font.init()
win = display.set_mode((600,500))
display.set_caption('Pin pong')
back = (155,234,123)
win_width = 600
win_height = 500





class GameSPrite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight,height))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSPrite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width-80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width-80:
            self.rect.y += self.speed
    
    
class Enemy(GameSPrite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0 
            self.rect.x = randint(80, win_width-80)



racket = Player('racket.png', 30,200,4,50,150)
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSPrite('tenis_ball.png',200,200,4,50,50)


speed_x = 3
speed_y = 3

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER1 LOSE!',True,(180,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER2 LOSE!',True,(180,0,0))


finish = False
run = True
while run:
    win.fill(back)
    for e in event.get():
        if e.type == QUIT:
            exit()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1

        if sprite.collide_rect(racket,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        
        if ball.rect.x < 0 :
            finish = True
            player1 = True
            win.blit(lose1,(200,200))
        if ball.rect.x > 600 :
            win.blit(lose2,(200,200))
            finish = True
            player2 = True
        racket.reset()
        racket.update_l()
        racket2.reset()
        racket2.update_r()
        ball.reset()
        ball.update()
    display.update()
    time.delay(20)
#display.update()
if player1:
    win.blit(lose1,(200,200))
if player2:
    win.blit(lose2,(200,200))
