# Разработай свою игру в этом файле!
from pygame import *

class GameSprite(sprite.Sprite):
  def __init__(self,picture,w,h,x,y)
      super().__init__()
      self.image=transform.scale(image.load(picture),(w,h))
      self.rect=self.image.get_rect()
      self.rect.x=x
      self.rect.y=y
  def reset(self):
    window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
  def __init__(self,picture,w,h,x_speed,y_speed):
       super().__init__(self)
       self.x_speed = x_speed
       self.y_speed = y_speed
  def update(self):
       self.rect.x += self.x_speed
       self.rect.y += self.y_speed
class Bullet(GameSprite):
  def __init(self,player_image,player_x,player_y,size_y,size_x,player_speed):
    GameSprite__init__(player_image,player_x,player_y,size_x,size_y)
    self.speed=player_speed

  def update(self):

    GameSprite


class Enemy(GameSprite):
  side = "left"
def__init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
  GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y,)
self.speed=player_speed

    def update(self):
      if self.rect.x <=420:
        self.side = "right"
      if self.rect.x >=615:
          self.side = "left"
      
      if self.side =="left":
          self.rect.x-=self.speed
      else:
          self.rect.x +=self.speed
    
class Bulet(GameSprite):
    def __init__(self,player_image,player_x,plaer_y,size_x,size_y)

        GameSprite,__init__(player_image,plaer_x,player_y,size_x,size_y)
        self.speed =player_speed

    def update(self):
      self.rect.x += self.speed
      if self.rect.x > 710:
        self.kill()



    
window=display.set_mode((700,500))
display.set_caption('Моя первая игра')
background = transform/scale(image.load('fon.jpg'),(700,500))

wall_1=GameSprite('wall.png',80,180,200,250)
player=Player('hero.png',50,50,0,0,0,0)
enemy=Enemy('enemy.jpg',80,80,620,80,5)

walls = sprite.Group()
walls.add(wall_1)

enemies = sprite.Group()
enemies.add(enemy1)

picture = transform.scale(image.load('background.jpg')),((700,500))
run=True
while run:
  for e in event.get():
    if e.type ==QUIT:
      run=False

    elif e.type== KEYDOWN:
      if e.key== K_LEFT:
        player.x_speed-=5
      elif e.key==K_RIGHT:
        player.x_speed +-5
      elif e.key==K_UP:
        player.y_speed-=5
      elif e.key==K_DOWN:
        player.y_speed+=5

    
    elif e.type== KEYUP:
      if e.key== K_LEFT:
        player.x_speed-=0
      elif e.key==K_RIGHT:
        player.x_speed +=0
      elif e.key==K_UP:
        player.y_speed-=0
      elif e.key==K_DOWN:
        player.y_speed+=0
        

  if sprite.collide_rect(player.enemy):
    player.rect.x=0
    player.rect.y=0
  if sprite.spritecollide(player,walls,False):
    player.x_speed *=-1
    player.y_speed *=-1
    
   if sprite.collide_rect(player,goal):
       goal.rect.x=radint(100,600)
       goal.rect.y=radint(100,400)

    if sprite.groupcollide(bullets,enemies,True,True):
        enemy3=Enemy('enemy.jpg',80,80,randint(100,600),randint(100,400),5)



player.update()
enemy.update()
player.reset()
enemy.reset()

  window.bilt(picture,(0,0))
display.update()




