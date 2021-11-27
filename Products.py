
from random import *
from pgzero.actor import Actor
from pygame import Rect

class ProductsImages():
    def __init__(self):
        # 阳光图片
        self.sun_images = []
        self.sun_images.extend([\
            "plants/sunflower/sun_1", \
            "plants/sunflower/sun_2", \
            "plants/sunflower/sun_3", \
            "plants/sunflower/sun_4", \
            "plants/sunflower/sun_5", \
            "plants/sunflower/sun_6", \
            "plants/sunflower/sun_7", \
            "plants/sunflower/sun_8", \
            "plants/sunflower/sun_9", \
            "plants/sunflower/sun_10", \
            "plants/sunflower/sun_11", \
            "plants/sunflower/sun_12", \
            "plants/sunflower/sun_13", \
            "plants/sunflower/sun_14", \
            "plants/sunflower/sun_15", \
            "plants/sunflower/sun_16", \
            "plants/sunflower/sun_17" \
            ])

        # 弹丸图片
        self.bullet_image = "plants/peashooter/bullet"
        self.firebullet_images = []
        self.firebullet_images.extend([\
            "plants/torchwood/fire_bullet1", \
            "plants/torchwood/fire_bullet2" \
            ])


class Sun(Actor):
    def __init__(self, T,L,images):
        Actor.__init__(self,image='plants/sunflower/sun_1')

        self.images = images.sun_images
        self.top, self.left = T, L
        self.rect1 = Rect(self.left, self.top, self.width, self.height) 
        self.rect2 = Rect(self.left, self.top, self.width, self.height) 
        self.rect1.left,self.rect1.top = randint(125,470), 87 - self.rect1.height
        self.rect2.centerx, self.rect2.centery = self.x, self.top + 30
        self.index_image = 0
        self.num_image = 17
        self.speed1 = 2
        self.speed2 = 1
        self.speed3 = 10
        self.position = randint(335, 480)
        self.count_time = 0
        self.is_supply = True   #系统提供True 向日葵生成False
        self.gather = False
        self.get_position = False

    def move1(self): #下落
        if self.top < self.position:
            self.top += self.speed1
        else:
            self.top = self.position

    def move2(self):#植物头顶
        #if self.rect2.centery > self.top - 10:
        #    self.rect2.centery -= self.speed2
        if self.top > self.position:
            self.top -= self.speed2
        else:
            #self.rect2.centery = self.top - 10
            self.top = self.position
    def move3(self):#gather
        if self.x > 79:
            self.x -= self.speed3
        else:
            self.x = 79
        if self.y > 36:
            self.y -= self.speed3
        else:
            self.y = 36
        if self.x == 79 and self.y == 36:
            self.get_position = True
        '''
        if self.is_supply:
            if self.rect1.centerx > 79:
                self.rect1.centerx -= self.speed3
            else:
                self.rect1.centerx = 79
            if self.rect1.centery > 36:
                self.rect1.centery -= self.speed3
            else:
                self.rect1.centery = 36
            if self.rect1.centerx == 79 and self.rect1.centery == 36:
                self.get_position = True
        else:
            if self.rect2.centerx > 79:
                self.rect2.centerx -= self.speed3
            else:
                self.rect2.centerx = 79
            if self.rect2.centery > 36:
                self.rect2.centery -= self.speed3
            else:
                self.rect2.centery = 36
            if self.rect2.centerx == 79 and self.rect2.centery == 36:
                self.get_position = True
        '''

class Bullet(Actor):
    def __init__(self,bg_size,positon,images):
        Actor.__init__(self,'plants/peashooter/bullet')

        self.bullet_image = images.bullet_image
        self.firebullet_images = images.firebullet_images
        self.rect = Rect(self.left, self.top, self.width, self.height) 
        self.index_image = 0
        self.num_image = 2
        self.left,self.top = positon[0] + 20,positon[1] - 28
        self.rect.left,self.rect.top = self.left,self.top
        self.screenwidth = bg_size[0]
        self.shoot = False
        self.speed = 5
        self.is_bullet = True
        #self.bullet_mask = pygame.mask.from_surface(self.bullet_image)
        #self.firebullet_mask = pygame.mask.from_surface(self.firebullet_images[0])
        #self.mask = self.bullet_mask

    def move(self):
        self.left += self.speed
        if self.left >= self.screenwidth:
            self.reset()

    def reset(self):
        self.left,self.top =self.rect.left, self.rect.top  
        self.is_bullet = True
        self.shoot = False