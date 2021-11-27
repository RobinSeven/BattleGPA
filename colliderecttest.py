from random import *
import sys
# import traceback
import Plants
import Products
import SeedBank
import LawnMower
import Zombies
import pgzrun
from pgzero.actor import Actor
import os
import time
#####################################################################################################################################
os.chdir(sys.path[0])
TITLE = '植物大战僵尸--freedom'
bg_size = WIDTH,HEIGHT = 800,600
ticktime =1
#原main文件main函数之前部分
# pygame初始化
# 创建窗口大小
#clock = pygame.time.Clock()

# 颜色
BLACK = (0,0,0)
RED = (255,0,0)
BAR_COLOR = (189,223,89)

# 植物种植范围
borderx = L, R = 30, 780
bordery = T, B = 90, 570
X = [75, 155, 235, 322, 406, 480, 562, 641, 720]
Y = [135, 225, 325, 427, 523]

plants_images = Plants.PlantsImages()
products_images = Products.ProductsImages()
plant = Plants.Torchwood(plants_images)
bullet = Products.Bullet(bg_size, (30,30),products_images)
def on_mouse_down(pos,button):
    pass
                                
def on_mouse_up(pos,button):
    pass

def on_mouse_move(pos, rel, buttons):
    pass

def update():
    plant.image = plant.images[0]
    plant.pos = (50,50)
    if bullet.colliderect(plant):
        print("colliderect")
def draw():   

    screen.clear()
    plant.draw()
    bullet.draw()



    
pgzrun.go()
