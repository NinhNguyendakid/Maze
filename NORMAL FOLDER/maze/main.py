#create a Maze game!
from pygame import*
from random import randint
# from PyQt5.QtWidgets import QApplication,QWidget
# app = QApplication([])
# screen = QWidget()
# screen.setWindowTitle('maze')
# screen.resize(750,500)
#Variables
WIDTH = 700
HEIGHT = 500
FPS = 60
COLOUR = (0,250,0)


class Main(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img),(20,20))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

# Player Class
class Player_cha(Main):
    def control(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 0   :
            self.rect.y -= self.speed

        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if key_pressed[K_RIGHT] and self.rect.x < WIDTH -50:
            self.rect.x += self.speed

        if key_pressed[K_DOWN] and self.rect.y < HEIGHT-50:
            self.rect.y += self.speed  

class Ghost(Main):
    direction = "left"
    
    def update(self):
        if self.rect.x <= 490:
            self.direction = "right"
        if self.rect.x >= WIDTH - 50:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed     

class Wall(sprite.Sprite):
    def __init__(self,x,y,color,w_width,w_height):
        super().__init__()
        self.image = Surface((w_width,w_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
    def build_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Coin(sprite.Sprite):
    def  __init__(self,img,x,y):
        super().__init__()
        self.rect = Rect(x,y,50,50)
        self.image = transform.scale(image.load(img),(50,50))
        
    def mint(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

font.init()
text = font.Font(None, 50)


win = text.render("You WIn", True, (0,255,0))
lose = text.render("You Lose",True,(255,0,0))
coin_count = 0

coin_c = text.render("Coin:",True,(255,255,255))
coin_c_text = text.render(str(coin_count),True,(255,255,255))

#Game window
window = display.set_mode((WIDTH,HEIGHT))
mixer.init()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
mixer.music.load("jungles.ogg")
mixer.music.play()
display.set_caption("Maze")
clock = time.Clock()




#Set scene background
background = transform.scale(image.load("background.jpg"),(WIDTH,HEIGHT))
player = Player_cha("hero.png",1, 25, 50)
enemy = Ghost("cyborg.png",2, 500, 350)
gold = Main("treasure.png", 0, 650,0)
wall_1 = Wall(1,0,COLOUR,10,400)
wall_2 = Wall(90,100,COLOUR,10,400)
wall_3 = Wall(0,0,COLOUR,700, 10)
wall_4 = Wall(0,490,COLOUR,700,10)
wall_5 = Wall(190,0,COLOUR,10, 400)
wall_6 = Wall(290,100,COLOUR,10,400)
wall_7 = Wall(390,0,COLOUR,10,400)
wall_8 = Wall(490,100,COLOUR,10,400)
wall_9 = Wall(590,0,COLOUR,10,350)
wall_10 = Wall(690,100,COLOUR,10,400)
#coin
coin_1 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_2 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_3 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_4 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_5 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_6 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_7 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_8 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_9 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
coin_10 = Coin("coin.png",randint(50,WIDTH-50),randint(50, HEIGHT-50))
#list
walls = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10]
coins = [coin_1,coin_2,coin_3,coin_4,coin_5,coin_6,coin_7,coin_8,coin_9,coin_10]

game = True
end = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            quit()

    if end != True:
        window.blit(background,(0,0))
        window.blit(coin_c,(25,25))
        window.blit(coin_c_text,(125,25))
        for coin in coins:
            coin.mint()
            
            if sprite.collide_rect(player,coin):
                money.play()
                coin_count += 1
                coins.remove(coin)
                coin.kill()
                coin_c_text = text.render(str(coin_count),True,(255,255,255))



        for wall in walls:
            wall.build_wall()
            if sprite.collide_rect(player, wall):
                kick.play()
                window.blit(lose,(WIDTH//2,HEIGHT//2))
                end = True

        if sprite.collide_rect(player,enemy):
            window.blit(lose,(WIDTH//2,HEIGHT//2))
            end = True

        if sprite.collide_rect(player,gold):
            window.blit(win,(WIDTH//2,HEIGHT//2))
            money.play()
            end = True  
        player.display()
        enemy.display()
        gold.display()
        
        
        player.control()
        enemy.update()
    else:
        end = False
        player = Player_cha("hero.png",10, 25, 50)
        time.delay(3000)

        

    display.update()
    clock.tick(FPS)
# screen.show()
# app.exec_()
