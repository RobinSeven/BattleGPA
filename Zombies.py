import pgzrun
from pgzero.actor import Actor
from random import *
import sys
import os
import pygame
os.chdir(sys.path[0])



class ZombiesImages():
    def __init__(self):
        self.oz1_images = []  # 原始僵尸1图片
        self.oz1_images.extend([ \
            "zombies/ordinaryzombie/zombie_0", \
            "zombies/ordinaryzombie/zombie_1", \
            "zombies/ordinaryzombie/zombie_2", \
            "zombies/ordinaryzombie/zombie_3", \
            "zombies/ordinaryzombie/zombie_4", \
            "zombies/ordinaryzombie/zombie_5", \
            "zombies/ordinaryzombie/zombie_6", \
            "zombies/ordinaryzombie/zombie_7", \
            "zombies/ordinaryzombie/zombie_8", \
            "zombies/ordinaryzombie/zombie_9", \
            "zombies/ordinaryzombie/zombie_10", \
            "zombies/ordinaryzombie/zombie_11", \
            "zombies/ordinaryzombie/zombie_12", \
            "zombies/ordinaryzombie/zombie_13", \
            "zombies/ordinaryzombie/zombie_14", \
            "zombies/ordinaryzombie/zombie_15", \
            "zombies/ordinaryzombie/zombie_16", \
            "zombies/ordinaryzombie/zombie_17", \
            "zombies/ordinaryzombie/zombie_18", \
            "zombies/ordinaryzombie/zombie_19", \
            "zombies/ordinaryzombie/zombie_20", \
            "zombies/ordinaryzombie/zombie_21" \
            ])

        self.oz2_images = []  # 原始僵尸2图片
        self.oz2_images.extend([ \
            "zombies/ordinaryzombie/zombie2_1", \
            "zombies/ordinaryzombie/zombie2_2", \
            "zombies/ordinaryzombie/zombie2_3", \
            "zombies/ordinaryzombie/zombie2_4", \
            "zombies/ordinaryzombie/zombie2_5", \
            "zombies/ordinaryzombie/zombie2_6", \
            "zombies/ordinaryzombie/zombie2_7", \
            "zombies/ordinaryzombie/zombie2_8", \
            "zombies/ordinaryzombie/zombie2_9", \
            "zombies/ordinaryzombie/zombie2_10", \
            "zombies/ordinaryzombie/zombie2_11", \
            "zombies/ordinaryzombie/zombie2_12", \
            "zombies/ordinaryzombie/zombie2_13", \
            "zombies/ordinaryzombie/zombie2_14", \
            "zombies/ordinaryzombie/zombie2_15", \
            "zombies/ordinaryzombie/zombie2_16", \
            "zombies/ordinaryzombie/zombie2_17", \
            "zombies/ordinaryzombie/zombie2_18", \
            "zombies/ordinaryzombie/zombie2_19", \
            "zombies/ordinaryzombie/zombie2_20", \
            "zombies/ordinaryzombie/zombie2_21", \
            "zombies/ordinaryzombie/zombie2_22", \
            "zombies/ordinaryzombie/zombie2_23", \
            "zombies/ordinaryzombie/zombie2_24", \
            "zombies/ordinaryzombie/zombie2_25", \
            "zombies/ordinaryzombie/zombie2_26", \
            "zombies/ordinaryzombie/zombie2_27", \
            "zombies/ordinaryzombie/zombie2_28", \
            "zombies/ordinaryzombie/zombie2_29", \
            "zombies/ordinaryzombie/zombie2_30", \
            "zombies/ordinaryzombie/zombie2_31" \
            ])

        self.oza_images = []  # 原始僵尸攻击图片
        self.oza_images.extend([ \
            "zombies/ordinaryzombie/zombieattack_0", \
            "zombies/ordinaryzombie/zombieattack_1", \
            "zombies/ordinaryzombie/zombieattack_2", \
            "zombies/ordinaryzombie/zombieattack_3", \
            "zombies/ordinaryzombie/zombieattack_4", \
            "zombies/ordinaryzombie/zombieattack_5", \
            "zombies/ordinaryzombie/zombieattack_6", \
            "zombies/ordinaryzombie/zombieattack_7", \
            "zombies/ordinaryzombie/zombieattack_8", \
            "zombies/ordinaryzombie/zombieattack_9", \
            "zombies/ordinaryzombie/zombieattack_10", \
            "zombies/ordinaryzombie/zombieattack_11", \
            "zombies/ordinaryzombie/zombieattack_12", \
            "zombies/ordinaryzombie/zombieattack_13", \
            "zombies/ordinaryzombie/zombieattack_14", \
            "zombies/ordinaryzombie/zombieattack_15", \
            "zombies/ordinaryzombie/zombieattack_16", \
            "zombies/ordinaryzombie/zombieattack_17", \
            "zombies/ordinaryzombie/zombieattack_18", \
            "zombies/ordinaryzombie/zombieattack_19", \
            "zombies/ordinaryzombie/zombieattack_20" \
            ])
        
        self.cz_images = []  # 帽子僵尸图片
        self.cz_images.extend([ \
            "zombies/coneheadzombie/coneheadzombie1", \
            "zombies/coneheadzombie/coneheadzombie2", \
            "zombies/coneheadzombie/coneheadzombie3", \
            "zombies/coneheadzombie/coneheadzombie4", \
            "zombies/coneheadzombie/coneheadzombie5", \
            "zombies/coneheadzombie/coneheadzombie6", \
            "zombies/coneheadzombie/coneheadzombie7", \
            "zombies/coneheadzombie/coneheadzombie8", \
            "zombies/coneheadzombie/coneheadzombie9", \
            "zombies/coneheadzombie/coneheadzombie10", \
            "zombies/coneheadzombie/coneheadzombie11", \
            "zombies/coneheadzombie/coneheadzombie12", \
            "zombies/coneheadzombie/coneheadzombie13", \
            "zombies/coneheadzombie/coneheadzombie14", \
            "zombies/coneheadzombie/coneheadzombie15", \
            "zombies/coneheadzombie/coneheadzombie16", \
            "zombies/coneheadzombie/coneheadzombie17", \
            "zombies/coneheadzombie/coneheadzombie18", \
            "zombies/coneheadzombie/coneheadzombie19", \
            "zombies/coneheadzombie/coneheadzombie20", \
            "zombies/coneheadzombie/coneheadzombie21" \
            ])

        self.cza_images = []  # 帽子僵尸攻击图片
        self.cza_images.extend([ \
            "zombies/coneheadzombie/coneheadzombieattack1", \
            "zombies/coneheadzombie/coneheadzombieattack2", \
            "zombies/coneheadzombie/coneheadzombieattack3", \
            "zombies/coneheadzombie/coneheadzombieattack4", \
            "zombies/coneheadzombie/coneheadzombieattack5", \
            "zombies/coneheadzombie/coneheadzombieattack6", \
            "zombies/coneheadzombie/coneheadzombieattack7", \
            "zombies/coneheadzombie/coneheadzombieattack8", \
            "zombies/coneheadzombie/coneheadzombieattack9", \
            "zombies/coneheadzombie/coneheadzombieattack10", \
            "zombies/coneheadzombie/coneheadzombieattack11" \
            ])

        self.bz_images = []  # 铁桶僵尸图片
        self.bz_images.extend([ \
            "zombies/bucketheadzombie/bucketheadzombie1", \
            "zombies/bucketheadzombie/bucketheadzombie2", \
            "zombies/bucketheadzombie/bucketheadzombie3", \
            "zombies/bucketheadzombie/bucketheadzombie4", \
            "zombies/bucketheadzombie/bucketheadzombie5", \
            "zombies/bucketheadzombie/bucketheadzombie6", \
            "zombies/bucketheadzombie/bucketheadzombie7", \
            "zombies/bucketheadzombie/bucketheadzombie8", \
            "zombies/bucketheadzombie/bucketheadzombie9", \
            "zombies/bucketheadzombie/bucketheadzombie10", \
            "zombies/bucketheadzombie/bucketheadzombie11", \
            "zombies/bucketheadzombie/bucketheadzombie12", \
            "zombies/bucketheadzombie/bucketheadzombie13", \
            "zombies/bucketheadzombie/bucketheadzombie14", \
            "zombies/bucketheadzombie/bucketheadzombie15" \
            ])

        self.bza_images = []  # 铁桶僵尸攻击图片
        self.bza_images.extend([ \
            "zombies/bucketheadzombie/bucketheadzombieattack1", \
            "zombies/bucketheadzombie/bucketheadzombieattack2", \
            "zombies/bucketheadzombie/bucketheadzombieattack3", \
            "zombies/bucketheadzombie/bucketheadzombieattack4", \
            "zombies/bucketheadzombie/bucketheadzombieattack5", \
            "zombies/bucketheadzombie/bucketheadzombieattack6", \
            "zombies/bucketheadzombie/bucketheadzombieattack7", \
            "zombies/bucketheadzombie/bucketheadzombieattack8", \
            "zombies/bucketheadzombie/bucketheadzombieattack9", \
            "zombies/bucketheadzombie/bucketheadzombieattack10", \
            "zombies/bucketheadzombie/bucketheadzombieattack11" \
            ])

        self.fz_images = []  # 举旗僵尸图片
        self.fz_images.extend([ \
            "zombies/flagzombie/flagzombie1", \
            "zombies/flagzombie/flagzombie2", \
            "zombies/flagzombie/flagzombie3", \
            "zombies/flagzombie/flagzombie4", \
            "zombies/flagzombie/flagzombie5", \
            "zombies/flagzombie/flagzombie6", \
            "zombies/flagzombie/flagzombie7", \
            "zombies/flagzombie/flagzombie8", \
            "zombies/flagzombie/flagzombie9", \
            "zombies/flagzombie/flagzombie10", \
            "zombies/flagzombie/flagzombie11", \
            "zombies/flagzombie/flagzombie12" \
            ])

        self.fza_images = []  # 举旗僵尸攻击图片
        self.fza_images.extend([ \
            "zombies/flagzombie/flagzombieattack1", \
            "zombies/flagzombie/flagzombieattack2", \
            "zombies/flagzombie/flagzombieattack3", \
            "zombies/flagzombie/flagzombieattack4", \
            "zombies/flagzombie/flagzombieattack5", \
            "zombies/flagzombie/flagzombieattack6", \
            "zombies/flagzombie/flagzombieattack7", \
            "zombies/flagzombie/flagzombieattack8", \
            "zombies/flagzombie/flagzombieattack9", \
            "zombies/flagzombie/flagzombieattack10", \
            "zombies/flagzombie/flagzombieattack11" \
            ])

        self.fzlh_images = []  # 举旗僵尸没有头图片
        self.fzlh_images.extend([ \
            "zombies/flagzombie/flagzombielosthead1", \
            "zombies/flagzombie/flagzombielosthead2", \
            "zombies/flagzombie/flagzombielosthead3", \
            "zombies/flagzombie/flagzombielosthead4", \
            "zombies/flagzombie/flagzombielosthead5", \
            "zombies/flagzombie/flagzombielosthead6", \
            "zombies/flagzombie/flagzombielosthead7", \
            "zombies/flagzombie/flagzombielosthead8", \
            "zombies/flagzombie/flagzombielosthead9", \
            "zombies/flagzombie/flagzombielosthead10", \
            "zombies/flagzombie/flagzombielosthead11", \
            "zombies/flagzombie/flagzombielosthead12" \
            ])
        

        self.zlh_images = []  # 原始僵尸没有头图片
        self.zlh_images.extend([ \
            "zombies/ordinaryzombie/zombielosthead1", \
            "zombies/ordinaryzombie/zombielosthead2", \
            "zombies/ordinaryzombie/zombielosthead3", \
            "zombies/ordinaryzombie/zombielosthead4", \
            "zombies/ordinaryzombie/zombielosthead5", \
            "zombies/ordinaryzombie/zombielosthead6", \
            "zombies/ordinaryzombie/zombielosthead7", \
            "zombies/ordinaryzombie/zombielosthead8", \
            "zombies/ordinaryzombie/zombielosthead9", \
            "zombies/ordinaryzombie/zombielosthead10", \
            "zombies/ordinaryzombie/zombielosthead11", \
            "zombies/ordinaryzombie/zombielosthead12", \
            "zombies/ordinaryzombie/zombielosthead13", \
            "zombies/ordinaryzombie/zombielosthead14", \
            "zombies/ordinaryzombie/zombielosthead15", \
            "zombies/ordinaryzombie/zombielosthead16", \
            "zombies/ordinaryzombie/zombielosthead17", \
            "zombies/ordinaryzombie/zombielosthead18" \
            ])

        self.zh_images = []  # 僵尸的头图片
        self.zh_images.extend([ \
            "zombies/ordinaryzombie/zombiehead1", \
            "zombies/ordinaryzombie/zombiehead2", \
            "zombies/ordinaryzombie/zombiehead3", \
            "zombies/ordinaryzombie/zombiehead4", \
            "zombies/ordinaryzombie/zombiehead5", \
            "zombies/ordinaryzombie/zombiehead6", \
            "zombies/ordinaryzombie/zombiehead7", \
            "zombies/ordinaryzombie/zombiehead8", \
            "zombies/ordinaryzombie/zombiehead9", \
            "zombies/ordinaryzombie/zombiehead10", \
            "zombies/ordinaryzombie/zombiehead11", \
            "zombies/ordinaryzombie/zombiehead12" \
            ])

        self.zlha_images = []  # 原始僵尸没有头攻击图片
        self.zlha_images.extend([ \
            "zombies/ordinaryzombie/zombielostheadattack1", \
            "zombies/ordinaryzombie/zombielostheadattack2", \
            "zombies/ordinaryzombie/zombielostheadattack3", \
            "zombies/ordinaryzombie/zombielostheadattack4", \
            "zombies/ordinaryzombie/zombielostheadattack5", \
            "zombies/ordinaryzombie/zombielostheadattack6", \
            "zombies/ordinaryzombie/zombielostheadattack7", \
            "zombies/ordinaryzombie/zombielostheadattack8", \
            "zombies/ordinaryzombie/zombielostheadattack9", \
            "zombies/ordinaryzombie/zombielostheadattack10", \
            "zombies/ordinaryzombie/zombielostheadattack11" \
            ])
        
        self.fzlha_images = []  # 举旗僵尸没有头攻击图片
        self.fzlha_images.extend([ \
            "zombies/flagzombie/flagzombielostheadattack1", \
            "zombies/flagzombie/flagzombielostheadattack2", \
            "zombies/flagzombie/flagzombielostheadattack3", \
            "zombies/flagzombie/flagzombielostheadattack4", \
            "zombies/flagzombie/flagzombielostheadattack5", \
            "zombies/flagzombie/flagzombielostheadattack6", \
            "zombies/flagzombie/flagzombielostheadattack7", \
            "zombies/flagzombie/flagzombielostheadattack8", \
            "zombies/flagzombie/flagzombielostheadattack9", \
            "zombies/flagzombie/flagzombielostheadattack10", \
            "zombies/flagzombie/flagzombielostheadattack11" \
            ])
        
        self.zd_images = []  # 僵尸死亡图片
        self.zd_images.extend([ \
            "zombies/ordinaryzombie/zombiedie1", \
            "zombies/ordinaryzombie/zombiedie2", \
            "zombies/ordinaryzombie/zombiedie3", \
            "zombies/ordinaryzombie/zombiedie4", \
            "zombies/ordinaryzombie/zombiedie5", \
            "zombies/ordinaryzombie/zombiedie6", \
            "zombies/ordinaryzombie/zombiedie7", \
            "zombies/ordinaryzombie/zombiedie8", \
            "zombies/ordinaryzombie/zombiedie9", \
            "zombies/ordinaryzombie/zombiedie10" \
            ])


class OrdinaryZombie(Actor):
    def __init__(self,x,Y,images):
        Actor.__init__(self,image='zombies/ordinaryzombie/zombie_0')

        self.x,self.y = x,Y[randint(0, 4)]

        self.oz_images = images.oz1_images  # 原始僵尸1图片
        self.index_oz_image = 0
        self.num_oz_image = 22
        #self.oz_mask = pygame.mask.from_surface(self.oz_images[11])

        self.za_images = images.oza_images  # 原始僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 21
        #self.za_mask = pygame.mask.from_surface(self.za_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        #self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        
        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])
        

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        #self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        #self.zd_rect = self.zd_images[0].get_rect()

        #self.rect = self.oz_images[0].get_rect()
        self.left, self.y = randint(self.x, 2 * self.x), self.y - 25
        self.index = 1
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 10
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        #self.mask = self.oz_mask

    def move(self):
        self.left -= self.speed

    def reset(self):
        self.left,self.y = randint(800, 2 * 800), self.y 
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 10
        self.attack = False
        self.willdie = False
        self.die = False
        #self.mask = self.oz_mask


class ConeheadZombie(Actor):
    def __init__(self,x,Y,images):
        Actor.__init__(self,'zombies/coneheadzombie/coneheadzombie1')

        self.x,self.y= x,Y[randint(0, 4)]

        self.oz_images = images.cz_images  # 帽子僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 21
        #self.oz_mask = pygame.mask.from_surface(self.oz_images[10])

        self.hoz_images = images.oz1_images  # 原始僵尸1图片
        self.index_hoz_image = 0
        self.num_hoz_image = 22
        #self.hoz_mask = pygame.mask.from_surface(self.hoz_images[11])

        self.za_images = images.cza_images  # 帽子僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        #self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.hza_images = images.oza_images  # 原始僵尸攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 21
        #self.hza_mask = pygame.mask.from_surface(self.hza_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        #self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        #self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        #self.zd_rect = self.zd_images[0].get_rect()

        #self.rect = self.oz_images[0].get_rect()
        self.left,self.y = randint(2 * self.x, 3 * self.x), self.y- 25
        self.index = 2
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 28
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        #self.mask = self.oz_mask

    def move(self):
        self.left -= self.speed

    def reset(self):
        self.left, self.y = randint(2 * 800, 3 * 800), self.y 
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 28
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        #self.mask = self.oz_mask


class BucketheadZombie(Actor):
    def __init__(self,x,Y,images):
        Actor.__init__(self,"zombies/bucketheadzombie/bucketheadzombie1")

        self.x, self.y = x, Y[randint(0, 4)] 

        self.oz_images = images.bz_images  # 铁桶僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 15
        #self.oz_mask = pygame.mask.from_surface(self.oz_images[7])

        self.hoz_images = images.oz2_images  # 原始僵尸2图片
        self.index_hoz_image = 0
        self.num_hoz_image = 31
        #self.hoz_mask = pygame.mask.from_surface(self.hoz_images[15])

        self.za_images = images.bza_images  # 铁桶僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        #self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.hza_images = images.oza_images  # 原始僵尸攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 21
        #self.hza_mask = pygame.mask.from_surface(self.hza_images[10])

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18
        #self.zlh_mask = pygame.mask.from_surface(self.zlh_images[9])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        #self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        #self.zd_rect = self.zd_images[0].get_rect()

        #self.rect = self.oz_images[0].get_rect()
        self.left,self.y = randint(3 * self.x, 4 * self.x), self.y - 25
        self.index = 3
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 64
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        #self.mask = self.oz_mask

    def move(self):
        self.left -= self.speed

    def reset(self):
        self.left, self.y = randint(3 * 800, 4 * 800), self.y
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.blood = 64
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        #self.mask = self.oz_mask


class FlagZombie(Actor):
    def __init__(self,x,Y,images):
        Actor.__init__(self,'zombies/flagzombie/flagzombie1')

        self.x,self.y = x,Y[randint(0, 4)]

        self.oz_images = images.fz_images  # 举旗僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 12
        #self.oz_mask = pygame.mask.from_surface(self.oz_images[6])

        self.za_images = images.fza_images  # 举旗僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11
        #self.za_mask = pygame.mask.from_surface(self.za_images[5])

        self.zlh_images = images.fzlh_images  # 举旗僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 12
        #self.zlh_mask = pygame.mask.from_surface(self.zlh_images[6])

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.fzlha_images  # 举旗僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11
        #self.zlha_mask = pygame.mask.from_surface(self.zlha_images[5])

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = Actor(self.zh_images[0])

        #self.rect = self.oz_images[0].get_rect()
        self.left, self.y = self.x, self.y - 25
        self.index = 4
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 1
        self.blood = 11
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        #self.mask = self.oz_mask

    def move(self):
        self.left -= self.speed