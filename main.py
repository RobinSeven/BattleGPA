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

# 载入游戏音乐与音效
'''
pygame.mixer.music.load("music/game.mp3")
pygame.mixer.music.set_volume(1)
chew_sound = pygame.mixer.Sound("music/chew.wav")
chew_sound.set_volume(0.3)
sungather_sound = pygame.mixer.Sound("music/sungather.wav")
sungather_sound.set_volume(0.7)
hit_sound = pygame.mixer.Sound("music/hit.wav")
hit_sound.set_volume(2)
gameover_sound = pygame.mixer.Sound("music/gameover.wav")
gameover_sound.set_volume(0.5)
'''
# 载入图片
zombies_images = Zombies.ZombiesImages()
plants_images = Plants.PlantsImages()
products_images = Products.ProductsImages()
car_image = LawnMower.CarImage()

def add_ordinaryzombies(group,num):
    for i in range(num):
        oz = Zombies.OrdinaryZombie(WIDTH, Y, zombies_images)
        group.append(oz)

def add_coneheadzombies(group,num):
    for i in range(num):
        cz = Zombies.ConeheadZombie(WIDTH, Y, zombies_images)
        group.append(cz)

def add_bucketheadzombies(group,num):
    for i in range(num):
        bz = Zombies.BucketheadZombie(WIDTH, Y, zombies_images)
        group.append(bz)

def add_flagzombies(group,num):
    for i in range(num):
        fz = Zombies.FlagZombie((WIDTH + 50), Y, zombies_images)
        group.append(fz)
#sound.gameover.play()
#music.play('game')


#######################################################################################################################################################
# 音频播放
open_music = True
open_sound = True
play_gameover_sound = False
#pygame.mixer.music.play(-1)
 # 准备植物组合
plantx=[]
# 种植的植物组合
plants=[]
# 产物集合
products = []

# 准备生成向日葵
sunflowerx = Plants.SunFlower(plants_images)
plantx.append(sunflowerx)
# 准备生成豌豆射手
peashooterx = Plants.Peashooter(plants_images)
plantx.append(peashooterx)
# 准备生成坚果
wallnutx = Plants.WallNut(plants_images)
plantx.append(wallnutx)
# 准备生成火炬
torchwoodx = Plants.Torchwood(plants_images)
plantx.append(torchwoodx)
torchwoods = [ ] # 用于与弹丸做碰撞检测
# 生成铲子
shovel = Plants.Shovel(plants_images)
plantx.append(shovel)


# 判断拖拽的图像是否出界
outborder = False

# 僵尸大波袭来
large_come = False
large_coming = False
large_time = 60 * ticktime
large_warn_time = 3 * ticktime

# 生成5辆小车
cars = []
cars_temp = []
for i in range(5):
    cars_temp.append(LawnMower.Car(L))
i = 0
for y in Y:
    cars_temp[i].y = y + 25
    i += 1
for c in cars_temp:
    cars.append(c)

# 僵尸组合
zombies = []
#order_zombies = []
# 生成僵尸
add_ordinaryzombies(zombies, 5)
add_coneheadzombies(zombies, 3)
add_bucketheadzombies(zombies, 2)

# 游戏界面
bg_image = Actor("others/background",topleft=(-200, 0))
bar_image = Actor("others/flagmeterempty",topleft=(WIDTH - 200, HEIGHT - 27))
bar_parts1_image = Actor("others/flagmeterparts1",topleft=(WIDTH - 68 - 1, HEIGHT - 32))
bar_parts2_image = Actor("others/flagmeterparts2",topleft=(WIDTH - 195, HEIGHT - 30))
largewave_image = Actor("others/largewave",center=(WIDTH // 2, HEIGHT // 2))
#largewave_rect = Rect(largewave_image.left, largewave_image.top,largewave_image.width,largewave_image.height)
#largewave_rect.centerx, largewave_rect.centery = WIDTH // 2, HEIGHT // 2
seedbank = SeedBank.SeedBank()



# 菜单界面
open_menu = False
menu_image = Actor("others/menu",center=(WIDTH // 2, HEIGHT // 2))  
#button_nor_image = Actor("others/button_nor")
#button_pressed_image = Actor("others/button_pressed")
button_image = Actor("others/button_nor",topright=(WIDTH, 0))
#button_image.right, button_image.top = WIDTH, 0
#button_rect = Rect(button_image.left, button_image.top,button_image.width,button_image.height)
#button_rect.right, button_rect.top = WIDTH, 0
resume_nor_image = Actor("others/resume_nor")
resume_pressed_image = Actor("others/resume_pressed")
resume_image = Actor("others/resume_nor")
resume_image.left, resume_image.top = 298, 408
#resume_rect = Rect(resume_image.left, resume_image.top,resume_image.width,resume_image.height)
#resume_rect.left, resume_rect.top = 298, 408
check_box_image1 = Actor("others/check_box",center=(450, 260))
check_box_image2 = Actor("others/check_box",center=(450, 297))
#check_box_rect1 = Rect(check_box_image.left, check_box_image.top,check_box_image.width,check_box_image.height)
#check_box_rect2 = Rect(check_box_image.left, check_box_image.top,check_box_image.width,check_box_image.height)
#check_box_rect1.centerx, check_box_rect1.centery = 450, 260
#check_box_rect2.centerx, check_box_rect2.centery = 450, 297
tick_image1 = Actor("others/tick",center=(450, 260))
tick_image2 = Actor("others/tick",center=(450, 297))
#tick_rect1 = Rect(tick_image.left, tick_image.top,tick_image.width,tick_image.height)
#tick_rect2 = Rect(tick_image.left, tick_image.top,tick_image.width,tick_image.height)
#tick_rect1.centerx, tick_rect1.centery = check_box_rect1.centerx, check_box_rect1.centery
#tick_rect2.centerx, tick_rect2.centery = check_box_rect2.centerx, check_box_rect2.centery
quitgame_nor_image = Actor("others/quitgame_nor")
quitgame_pressed_image = Actor("others/quitgame_pressed")
quitgame_image = Actor("others/quitgame_nor")
quitgame_image.left, quitgame_image.top = 318, 352
#quitgame_rect = Rect(quitgame_image.left, quitgame_image.top,quitgame_image.width,quitgame_image.height)
#quitgame_rect.left, quitgame_rect.top = 318, 352
# 游戏结束界面
gameover = False
open_quit_window = False
zombiewon_display_time = 7 * ticktime
zombiewon_image = Actor("others/zombieswon")
zombiewon_rect = Rect(zombiewon_image.left, zombiewon_image.top,zombiewon_image.width,zombiewon_image.height)
zombiewon_rect.centerx, zombiewon_rect.centery = WIDTH // 2, HEIGHT // 2
quit_window_image = Actor("others/exit_window",center=(WIDTH // 2, HEIGHT // 2))
#quit_window_rect = Rect(quit_window_image.left, quit_window_image.top,quit_window_image.width,quit_window_image.height)
#quit_window_rect.centerx, quit_window_rect.centery = WIDTH // 2, HEIGHT // 2
quit_nor_image = Actor("others/quit_nor")
quit_pressed_image = Actor("others/quit_pressed")
quit_image = Actor("others/quit_nor",center=(WIDTH // 2 ,380))
quit_rect =  Rect(quit_image.left, quit_image.top,quit_image.width,quit_image.height)
quit_rect.centerx, quit_rect.centery = WIDTH // 2 ,380

# 游戏开始界面
start = False
start_ready = False
open_help = False
start_bg_image = Actor("others/start_background")
start_nor_image = Actor("others/start_nor",topleft=(467,86))
start_pressed_image = Actor("others/start_pressed",topleft=(467,86))
start_image = start_nor_image
#start_rect =  Rect(start_image.left, start_image.top,start_image.width,start_image.height)
#start_rect.left, start_rect.top = 467,86
game_logo_image = Actor("others/game_logo")
#game_logo_rect = Rect(game_logo_image.left, game_logo_image.top,game_logo_image.width,game_logo_image.height)
game_logo_image.left, game_logo_image.top = 13, -game_logo_image.height
exit_nor_image = Actor("others/exit_nor",topleft=(730, 515))
exit_pressed_image = Actor("others/exit_pressed",topleft=(730, 515))
exit_image = exit_nor_image
exit_rect =  Rect(exit_image.left, exit_image.top,exit_image.width,exit_image.height)
exit_rect.left, exit_rect.top = 730, 515
help_nor_image = Actor("others/help_nor",topleft=(667, 526))
help_pressed_image = Actor("others/help_pressed",topleft=(667, 526))
help_image = help_nor_image
help_rect =  Rect(help_image.left, help_image.top,help_image.width,help_image.height)
help_rect.left, help_rect.top = 667, 526
option_nor_image = Actor("others/option_nor",topleft=(607, 489))
option_pressed_image = Actor("others/option_pressed",topleft=(607, 489))
option_image = option_nor_image
option_rect = Rect(option_image.left, option_image.top,option_image.width,option_image.height)
option_rect.left, option_rect.top = 607, 489
help_doc_image = Actor("others/help",center=(WIDTH // 2, HEIGHT // 2))
help_doc_rect = Rect(help_doc_image.left, help_doc_image.top,help_doc_image.width,help_doc_image.height)
help_doc_rect.centerx, help_doc_rect.centery = WIDTH // 2, HEIGHT // 2
off_help_image = Actor("others/off_help",topleft=( 615, 120))
off_help__rect = Rect(off_help_image.left, off_help_image.top,off_help_image.width,off_help_image.height)
off_help__rect.left, off_help__rect.top = 615, 120
prepare_tip_images = []
prepare_tip_images.extend([\
    "others/preparegrowplants1", \
    "others/preparegrowplants2", \
    "others/preparegrowplants3" \
    ])
prepare_tip_rect = Actor("others/preparegrowplants1",center=(WIDTH // 2, HEIGHT // 2))
#prepare_tip_rect.centerx, prepare_tip_rect.centery = WIDTH // 2, HEIGHT // 2
index_prepare_tip_image = -1
num_prepare_tip_image = 3

# 植物影子图片
plantshadow = Actor("others/plantshadow")
################################################
# 阳光数量
sun_num = 5000
#sun_num_font = pygame.font.Font("font/corisandebold.otf",19)
#screen.draw.text("Font name and size", (20, 100), fontname="Boogaloo", fontsize=60)
COLOR = BLACK
# 阳光集合
suns = []

# 阳光补给和消失时间
supply_time = 6* ticktime
disappear_time1 = 12* ticktime
disappear_time2 = 8* ticktime

# 计时器
count_time = 0
#COUNT_TIME = USEREVENT
#pygame.time.set_timer(COUNT_TIME,1 * 1000)

# 弹丸集合
bullets = []

# 用于切换图片
delay_1 = 5 
delay_2 = 8 
delay_3 = 50 

# 是否选中植物
select = 0

# 游戏进度条长度
bar_length = 1
########################################################################################
#从卡片拖动生成植物用
pos_price=0
pos_image = Actor('plants/sunflower/sunflower1')   #原来用矩形(pos_rect,pos_image)记录准备生成植物的拖动图象，改为用Actor
darw_pos_image = False
plant_index = 0

def on_mouse_down(pos,button):
    global select
    global pos_image
    global pos_price
    global plant_index
    global open_menu
    global open_help
    global gameover
    global start_ready
    global start
    global open_sound
    global open_music
    # 选择植物卡片
    if not open_menu and not gameover and start_ready:
        for px in plantx:
            if button == mouse.LEFT  and px.collidepoint(pos):
                plant_index = px.index
                pos_image.image = px.images[0]
                #pos_rect = px.rect    原来用矩形记录
                pos_image.pos = pos
               
                pos_price = px.price
                if sun_num < pos_price:
                    COLOR = RED
                select = 1
            if select == 1:
                if button == mouse.RIGHT and pos_image.collidepoint(pos):
                    select = 0
    # 收集阳光
    if not open_menu and not gameover and start_ready: #
        for s in suns:
            if button==mouse.LEFT and s.collidepoint(pos):
                s.gather = True
                if open_sound:
                    sounds.sungather.play()
            '''
            if s.is_supply:
                if button==mouse.LEFT and s.collidepoint(pos):
                    s.gather = True
                    if open_sound:
                    #    sungather_sound.play()
                        sounds.sungather.play()

            else:
                if button==mouse.LEFT and s.collidepoint(pos):
                    s.gather = True
                    if open_sound:
                        sounds.sungather.play()
            '''
 # 菜单操作
    if not gameover and start_ready:
        if button == mouse.LEFT  and button_image.collidepoint(pos):
            open_menu = True
        if button == 1 and quitgame_image.collidepoint(pos) and open_menu:
            #pygame.quit()
            sys.exit()
    if not gameover:
        if button == 1 and resume_image.collidepoint(pos):
            open_menu = False
        if button == 1 and check_box_image1.collidepoint(pos) and open_menu:
            if open_sound:
                open_sound = False
            else:
                open_sound = True
        if button == 1 and check_box_image2.collidepoint(pos) and open_menu:
            if open_music:
                open_music = False
                #music.play('game')
                music.pause()
            else:
                open_music = True
                music.unpause()
    # 游戏初始界面操作 
    if not start:
        if button == 1 and start_image.collidepoint(pos) and not open_menu and not open_help:
            start = True
        if button == 1 and exit_image.collidepoint(pos) and not open_menu and not open_help:
            
            sys.exit()
        if button == 1 and help_image.collidepoint(pos) and not open_menu:
            open_help = True
        if button == 1 and off_help_image.collidepoint(pos) and open_help:
            open_help = False
        if button == 1 and option_image.collidepoint(pos) and not open_help:
            open_menu = True
    # 游戏结束窗口操作
    if gameover:
        if button == 1 and quit_image.collidepoint(pos):
            
            sys.exit()
                                
def on_mouse_up(pos,button):
    global darw_pos_image
    global select
    global sun_num
    global  bullets 
    global  products

    darw_pos_image = False
    if not open_menu and not gameover and start_ready:
        if button == mouse.LEFT:
            if select == 1:
                if not outborder:
                    # 生成植物
                    if plant_index == 1:
                        plant = Plants.SunFlower(plants_images)
                    if plant_index == 2:
                        plant = Plants.Peashooter(plants_images)
                    if plant_index == 3:
                        plant = Plants.WallNut(plants_images)
                    if plant_index == 4:
                        plant = Plants.Torchwood(plants_images)
                    if plant_index == 5:
                        plant = Plants.Shovel(plants_images)
                    plant.pos = pos
                    plant.image = plant.images[0]
                    # 位置调整
                    minx = X[0]
                    miny =Y[0]
                    for x in X:
                        if abs(plant.x - x) < abs(plant.x - minx):
                            minx = x
                    plant.x = minx
                    for y in Y:
                        if abs(plant.y - y) < abs(plant.y - miny):
                            miny = y
                    plant.y = miny
                    # 检查位置是否已有植物
                    have_plant = False
                    for p in plants:
                        if (plant.x == p.x) and \
                                (plant.y == p.y):
                            have_plant = True
                            if plant_index == 5:
                                plants.remove(p)
                                if p.index == 4:
                                    torchwoods.remove(p)
                                if p.index == 2:
                                    for b in bullets:
                                        if (b.left == p.x + 20) and (b.top == p.y - 28):
                                            bullets.remove(b)
                                            products.remove(b)
                    if not have_plant and (plant_index != 5) and (sun_num >= plant.price):
                        plants.append(plant)
                        sun_num -= plant.price
                        if plant.index == 4:
                            torchwoods.append(plant)
                        # 豌豆射手生成弹丸
                        if plant.index == 2:
                            bullet = Products.Bullet(bg_size, plant.pos,products_images)
                            bullets.append(bullet)
                            products.append(bullet)
                select = 0
                COLOR = BLACK


def on_mouse_move(pos, rel, buttons):
    #global select
    global button_image
    global resume_image
    global quitgame_image
    global quit_image
    global start_image
    global exit_image
    global help_image
    global option_image

    global pos_image
    global darw_pos_image
    global outborder
    # 所以button的按压样式
    if button_image.collidepoint(pos) and not open_menu:
        button_image.image = "others/button_pressed"
    else:
        button_image.image = "others/button_nor"
    if resume_image.collidepoint(pos) and open_menu:
        resume_image.image = "others/resume_pressed"
    else:
        resume_image.image = "others/resume_nor"
    if quitgame_image.collidepoint(pos) and start_ready:
        quitgame_image.image = "others/quitgame_pressed"
    else:
        quitgame_image.image  = "others/quitgame_nor"
    if quit_image.collidepoint(pos) and gameover:
        quit_image.image  = "others/quit_pressed"
    else:
        quit_image.image  = "others/quit_nor"
    if start_image.collidepoint(pos) and not start and not open_menu and not open_help:
        start_image.image  = "others/start_pressed"
    else:
        start_image.image  = "others/start_nor"
    if exit_image.collidepoint(pos) and not start and not open_menu and not open_help:
        exit_image.image  = "others/exit_pressed"
    else:
        exit_image.image  = "others/exit_nor"
    if help_image.collidepoint(pos) and not start and not open_menu and not open_help:
        help_image.image  = "others/help_pressed"
    else:
        help_image.image  = "others/help_nor"
    if option_image.collidepoint(pos) and not start and not open_menu and not open_help:
        option_image.image  = "others/option_pressed"
    else:
        option_image.image  = "others/option_nor"
    
    # 绘制拖拽的植物图像
    if mouse.LEFT in buttons: 
        if not gameover:
            if select == 1 and (sun_num >= pos_price):
                darw_pos_image = True
                pos_image.pos = pos
                #pos_image.draw()
                #screen.blit(pos_image.image, pos)
                if (pos_image.x < L or pos_image.x > R or pos_image.y < T or pos_image.y > B):
                    outborder = True
                else:
                    outborder = False

clockcount = 0
def up_clock_count():
    global clockcount
    clockcount+=1
    #print(clockcount)

clock.schedule_interval(up_clock_count, 1.0)

def update():
    global count_time
    global delay_1  
    global delay_2  
    global delay_3
    global large_coming
    global bar_length
    global large_come
    global large_time
    global large_warn_time
    global zombiewon_display_time
    global gameover
    global index_prepare_tip_image 
    #global num_prepare_tip_image 
    global clockcount
    if clockcount == count_time: #每秒=1次        
        if not gameover:
            count_time += 1
            # 游戏进度条----449~543

            if not large_coming:
                bar_length += 1
                if bar_length == 128:
                    large_coming = True
                    if not large_come:
                        large_come = True
                        # 生成举旗僵尸
                        add_flagzombies(zombies, 2)
                        # 僵尸大波袭来位置改变
                        i = 0
                        for z in zombies:
                            if z.left > WIDTH:
                                z.left = WIDTH + 50 + (i * 20)
                                i += 1
                                if i > 5:
                                    i = 0
                else:
                    large_coming = False
                if bar_length > 128:
                    bar_length = 1
            # 僵尸大波袭来时间
            if large_coming:
                large_time -= 1 * ticktime
                large_warn_time -= 1 * ticktime
                if large_time == 0:
                    large_coming = False
                    large_come = False
                    large_time = 60 * ticktime
                    large_warn_time = 3 * ticktime
                    # 增加僵尸数量
                    add_ordinaryzombies(zombies,5)
                    add_coneheadzombies(zombies,3)
                    add_bucketheadzombies(zombies,2)
            # 弹丸发射
            for p in plants:
                for z in zombies:
                    if (z.right > p.right) and (z.x < WIDTH) \
                            and (z.y == p.y - 25) and not z.die:
                        for b in bullets:
                            if (b.left == p.x + 20) and (b.top == p.y - 28):
                                b.shoot = True   
            # 生成阳光
            if (count_time % supply_time == 0):
                sun = Products.Sun(9, randint(125,470),products_images)
                suns.append(sun)
                products.append(sun)

            for s in suns:
                s.count_time += 1
            for p in plants:
                if p.index == 1:
                    p.count_time += 1 * ticktime
                    if (p.count_time % p.create_time == 0):
                        sun = Products.Sun(p.top, p.left,products_images)
                        sun.is_supply = False
                        sun.position = p.top-50
                        sun.count_time = 1 * ticktime
                        suns.append(sun)
                        products.append(sun)
            for s in suns:
                if (s.count_time % disappear_time1 == 0) and s.is_supply:
                    suns.remove(s)
                    products.remove(s)
                if (s.count_time % disappear_time2 == 0) and not s.is_supply:
                    suns.remove(s)
                    products.remove(s)
            # 植物被攻击
            for p in plants:
                if p.attacked:
                    for i in range(p.num_az):
                        p.blood -= 1
                        if open_sound:
                            sounds.chew.play()
                        if p.blood == 26 and p.index == 3:
                            p.images = p.c1_images
                            p.index_image = p.index_c1_image
                            p.num_image = p.num_c1_image
                            #p.mask = p.c1_mask
                        if p.blood == 13 and p.index == 3:
                            p.images = p.c2_images
                            p.index_image = p.index_c2_image
                            p.num_image = p.num_c2_image
                            #p.mask = p.c2_mask
                        if p.blood == 0:
                            plants.remove(p)
                            if p.index == 2:
                                for b in bullets:
                                    if (b.left == p.x + 20) and (b.top == p.y - 28):
                                        bullets.remove(b)
                                        products.remove(b)
                            if p.index == 4:
                                torchwoods.remove(p)
        else:
            zombiewon_display_time -= 1
            if zombiewon_display_time == 0:
                open_quit_window = True


    if start_ready:
        if not open_menu and not gameover:
            # 检测植物是否被僵尸攻击
            for p in plants:
                attack_zombies = []
                num_attack = 0
                for z in zombies:
                    if (z.y == p.y - 25) and not z.die:
                        #attack_zombies.append(z)
                        zrect = Rect(z.left+75,z.top,z.width,z.height)
                        if p.colliderect(zrect):
                            num_attack+=1
                #num_attack = pygame.sprite.spritecollide(p,attack_zombies,False,pygame.sprite.collide_mask)
                for i in attack_zombies:
                    attack_zombies.remove(i)
                
                if num_attack:
                    p.attacked = True
                    p.num_az = num_attack
                else:
                    p.attacked = False
                    p.num_az = 0
                
            # 检测僵尸是否攻击植物
            for z in zombies:
                attacked_plants = []
                attack = 0
                for p in plants:
                    if (z.y == p.y - 25):
                        #attacked_plants.append(p)
                        zrect = Rect(z.left+75,z.top,z.width,z.height)
                        if p.colliderect(zrect):
                            attack +=1
                #attack = pygame.sprite.spritecollide(z,attacked_plants,False,pygame.sprite.collide_mask)
                
                for i in attacked_plants:
                    attacked_plants.remove(i)
                if attack:
                    if not z.attack and not z.willdie:
                        z.attack = True
                        z.left -= 10
                        if z.index == 1 or z.index == 4:
                            z.images = z.za_images
                            z.index_image = z.index_za_image
                            z.num_image = z.num_za_image
                            #z.mask = z.za_mask
                        if (z.index == 2 or z.index == 3) and z.hat:
                            z.images = z.za_images
                            z.index_image = z.index_za_image
                            z.num_image = z.num_za_image
                            #z.mask = z.za_mask
                        if (z.index == 2 or z.index == 3) and not z.hat:
                            z.images = z.hza_images
                            z.index_image = z.index_hza_image
                            z.num_image = z.num_hza_image
                            #z.mask = z.hza_mask
                    if not z.attack and z.willdie:
                        z.attack = True
                        z.left -= 10
                        z.images = z.zlha_images
                        z.index_image = z.index_zlha_image
                        z.num_image = z.num_zlha_image
                        #z.mask = z.zlha_mask
                else:
                    if z.attack and not z.willdie:
                        z.attack = False
                        if z.index == 1 or z.index == 4:
                            z.images = z.oz_images
                            z.index_image = z.index_oz_image
                            z.num_image = z.num_oz_image
                            #z.mask = z.oz_mask
                        if (z.index == 2 or z.index == 3) and z.hat:
                            z.images = z.oz_images
                            z.index_image = z.index_oz_image
                            z.num_image = z.num_oz_image
                            #z.mask = z.oz_mask
                        if (z.index == 2 or z.index == 3) and not z.hat:
                            z.images = z.hoz_images
                            z.index_image = z.index_hoz_image
                            z.num_image = z.num_hoz_image
                            #z.mask = z.hoz_mask
                    if z.attack and z.willdie:
                        z.attack = False
                        z.images = z.zlh_images
                        z.index_image = z.index_zlh_image
                        z.num_image = z.num_zlh_image
                        #z.mask = z.zlh_mask

            # 检测僵尸是否被弹丸攻击
            for z in zombies:
                shoot_bullets =[]   # shoot=True
                attack_bullets = []
                for b in bullets:
                    if b.shoot:
                        #shoot_bullets.append(b)
                        if not z.die:
                            zrect = Rect(z.left+75,z.top,z.width,z.height)
                            if b.colliderect(zrect) :
                                attack_bullets.append(b)
                                #print(b.left,b.top,b.width,b.height)
                                #print(z.left,z.top,z.width,z.height)
                
                if not z.die:
                    pass
                    #attack_bullets = pygame.sprite.spritecollide(z, shoot_bullets, False, pygame.sprite.collide_mask)
                for i in shoot_bullets:
                    shoot_bullets.remove(i)
                for ab in attack_bullets:
                    if open_sound:
                        sounds.hit.play()
                    if ab.is_bullet:
                        z.blood -= 1
                    else:
                        z.blood -= 2
                    ab.reset()
                    if (z.blood == 11 or z.blood == 10) and (z.index == 2 or z.index == 3):
                        if z.hat:
                            z.hat = False
                            if z.attack:
                                z.images = z.hza_images
                                z.index_image = z.index_hza_image
                                z.num_image = z.num_hza_image
                                #z.mask = z.hza_mask
                            else:
                                z.images = z.hoz_images
                                z.index_image = z.index_hoz_image
                                z.num_image = z.num_hoz_image
                                #z.mask = z.hoz_mask

                    if (z.blood == 2 or z.blood == 1) and not z.willdie:
                        z.willdie = True
                        
                        z.zh_rect.x,z.zh_rect.y = z.x + 50,z.y - 20
                        if z.attack:
                            z.images = z.zlha_images
                            z.index_image = z.index_zlha_image
                            z.num_image = z.num_zlha_image
                            # z.mask = z.zlha_mask
                        if not z.attack:
                            z.images = z.zlh_images
                            z.index_image = z.index_zlh_image
                            z.num_image = z.num_zlh_image
                            # z.mask = z.zlh_mask
                        
                    if z.blood <= 0:
                        z.die = True
                        #z.zd_rect =  Rect(z.left,z.top,z.width,z.height)
                        z.images = z.zd_images  # 原始僵尸1图片
                        z.index_image = z.index_zd_image
                        z.num_image = z.num_zd_image


            # 检测僵尸是否与小车碰撞
            for z in zombies:
                check_cars = []
                for c in cars:
                    if c.right <= WIDTH and (c.y - 25 == z.y + 25):
                        #check_cars.append(c)
                        if not z.die:                            
                            zrect = Rect(z.left+75,z.top,z.width,z.height)
                            if c.colliderect(zrect):
                                c.active = True
                                z.die = True
                                #z.zd_rect = z.rect

                '''
                if not z.die:
                    pass
                    #collide_cars = pygame.sprite.spritecollide(z,check_cars,False,pygame.sprite.collide_mask)
                for i in check_cars:
                    check_cars.remove(i)
                
                for cc in collide_cars:
                    cc.active = True
                
                if collide_cars:
                    z.die = True
                    z.zd_rect = z.rect
                '''
            '''
            # 将僵尸从上往下排序
            order_zombies = []
            for z in zombies:
                order_zombies.append(z)
            num = len(order_zombies)
            for i in range(num):
                index_top = i
                zombie_top = order_zombies[i]
                for j in range(i+1,num):
                    if zombie_top.y > order_zombies[j].y:
                        index_top = j
                        zombie_top = order_zombies[j]
                order_zombies[index_top] = order_zombies[i]
                order_zombies[i] = zombie_top
            '''
            # 检测弹丸是否穿过火炬
            for b in bullets:
                if b.shoot:
                    if b.is_bullet:      
                        through=False                  
                        for t in torchwoods:
                            if b.colliderect(t._rect):
                                #print(t._rect,b._rect)
                                through=True                        
                            
                        #through = pygame.sprite.spritecollide(b, torchwoods, False, pygame.sprite.collide_mask)
                    else:
                        through = True
                    if through:
                        b.is_bullet = False
                        #print("through")
                        #b.mask = b.firebullet_mask
                    else:
                        b.is_bullet = True
                        #b.mask = b.bullet_mask

            # 检测僵尸是否进入房子（游戏结束）
            for z in zombies:
                if z.right < 0 and not z.die:
                    gameover = True
                    z.bottom = 400
                    z.get_win = True
            if gameover:
                for z in zombies:
                    if z.left < 0 and not z.get_win:
                        z.x = L    

        


# 图片索引值、摆动帧率
    if not open_menu and start:
        if not gameover:
            for p in plants:
                if delay_1 == 5:
                    p.index_image += 1
                if p.index_image == p.num_image:
                    p.index_image = 0
                p.image = p.images[p.index_image]
            for pr in products:
                if delay_1 == 5:
                    pr.index_image += 1
                if pr.index_image == pr.num_image:
                    pr.index_image = 0
                #pr.image = pr.images[pr.index_image]
        for z in zombies:
            if not gameover or z.get_win:
                if z.willdie:
                    if delay_1 == 5 and (z.index_zh_image < z.num_zh_image + 10):
                        z.index_zh_image += 1
                if z.die:
                    if delay_2 == 8 and (z.index_zd_image < z.num_zd_image + 8):
                        z.index_zd_image += 1
                if delay_1 == 5:
                    z.index_image += 1
                if z.index_image == z.num_image:
                    z.index_image = 0
        delay_1 -= 1
        delay_2 -= 1
        if delay_1 == 0:
            delay_1 = 5
        if delay_2 == 0:
            delay_2 = 8

    if not start_ready and start and cars_temp[0].right == L + 4:
        delay_3 -= 1
        if delay_3 == 0:
            delay_3 = 50
        if delay_3 == 50:
            index_prepare_tip_image += 1
    #print(delay_3)
    #print(index_prepare_tip_image)
def draw():   
    global bg_rect
    global sun_num
    global gameover
    global start_ready
    global start
    global select
    global zombiewon_display_time
    global count_time
    global clockcount
    global index_prepare_tip_image
    global play_gameover_sound
    #if clockcount != count_time:
    #    return
    screen.clear()

# 绘制游戏初始界面
# 绘制游戏背景
# 绘制游戏进度条
# 绘制卡片栏
# 绘制5辆小车
# 绘制准备种植植物提示
# 绘制植物
# 绘制僵尸
# 绘制弹丸
# 绘制拖拽的植物图像
# 绘制阳光
# 绘制僵尸大波袭来warn
# 绘制游戏结束画面
# 绘制阳光数量
# 绘制菜单界面

    if not start: #(放入draw)
        # 绘制游戏初始界面
        #pygame.mixer.music.pause()
        start_bg_image.draw()
        game_logo_image.draw()
        game_logo_image.top += 10
        if game_logo_image.top > 8:
            game_logo_image.top = 8
        
        start_image.draw() 
        exit_image.draw()
        help_image.draw()
        option_image.draw()
        if open_help:
            help_doc_image.draw()
            off_help_image.draw()
     
    
    else:
        # 绘制游戏背景
        if gameover:
            speed = 5
            bg_image.left += speed
            if bg_image.left > 0:
                bg_image.left = 0
            else:
                # 调整所有对象位置
                for p in plants:
                    p.left += speed
                for z in zombies:
                    z.left += speed
                    z.zh_rect.left += speed
                for s in suns:
                    if s.is_supply:
                        s.rect1.left += speed
                    else:
                        s.rect2.left += speed
                for b in bullets:
                    b.left += speed
                for c in cars:
                    c.left += speed
        bg_image.draw()
        #screen.blit(bg_image,bg_rect)    

        if not gameover:
            # 绘制游戏进度条
            if start_ready:
                bar_image.draw()
                bar_parts2_image.draw()
                #draw.line(start, end, (r, g, b))
                #draw.filled_rect(rect, (r, g, b))
                screen.draw.line((WIDTH - 51 - bar_length, HEIGHT - 17),(WIDTH - 51,HEIGHT - 17), BAR_COLOR)
                #screen.blit(bar_parts1_image,(width - 68 - bar_length, height - 32))
                bar_parts1_image.left = WIDTH - 68 - bar_length
                bar_parts1_image.draw()              

            # 绘制卡片栏            
            if not open_menu and not gameover:
                seedbank.move()
            seedbank.draw()
            # 绘制卡片栏里的卡片
            if seedbank.position:
                for px in plantx:
                    px.image=px.card_image
                    px.draw()
                    #screen.blit(px.card_image,px.card_rect)

        # 绘制5辆小车
        if seedbank.position:
            for c in cars:
                if not open_menu and not gameover:
                    if not c.active:
                        c.move1()
                    else:
                        c.move2()
                c.draw()
                #screen.blit(c.image,c.rect)
                if c.left > WIDTH:
                    cars.remove(c)
        
        if not start_ready:
            # 绘制准备种植植物提示
            if -1 < index_prepare_tip_image < 3 and cars_temp[0].right == L + 4:
                prepare_tip_rect.image = prepare_tip_images[index_prepare_tip_image]
                prepare_tip_rect.draw()
                #screen.blit(prepare_tip_images[index_prepare_tip_image], prepare_tip_rect)
            if index_prepare_tip_image >= 3:
                start_ready = True
                if open_music:
                    music.play('game')
        else:
#803
            # 绘制植物
            for p in plants:
                p.draw()
            #screen.blit(plantshadow, (p.rect.left + p.shadow_rectx, p.rect.top + p.shadow_recty))
            #screen.blit(p.images[p.index_image], p.rect)    
    
            # 将僵尸从上往下排序
            order_zombies = []
            for z in zombies:
                order_zombies.append(z)
            num = len(order_zombies)
            for i in range(num):
                index_top = i
                zombie_top = order_zombies[i]
                for j in range(i+1,num):
                    if zombie_top.y > order_zombies[j].y:
                        index_top = j
                        zombie_top = order_zombies[j]
                order_zombies[index_top] = order_zombies[i]
                order_zombies[i] = zombie_top
    

            # 绘制僵尸
            for z in order_zombies:
                if not z.die:
                    if delay_1 == 5 and not z.attack:
                        if not open_menu and not gameover:
                            z.move()
                    z.image = z.images[z.index_image]
                    z.draw()
                    #screen.blit(z.images[z.index_image], z.rect)
                else:
                    if (z.index_zd_image < z.num_zd_image + 8):
                        index2 = z.index_zd_image
                        if z.index_zd_image >= z.num_zd_image:
                            index2 = z.num_zd_image - 1
                        z.image = z.zd_images[index2]
                        z.draw()
                        #screen.blit(z.zd_images[index2], z.zd_rect)
                    else:
                        if z.index == 4:
                            zombies.remove(z)
                        else:
                            z.reset()
                if z.willdie and (z.index_zh_image < z.num_zh_image + 10):
                    index1 = z.index_zh_image
                    if z.index_zh_image >= z.num_zh_image:
                        index1 = z.num_zh_image - 1
                    #screen.blit(z.zh_images[index1], z.zh_rect)
                    z.image = z.zh_images[index1]
                    z.draw()

            # 绘制弹丸
            #print(len(bullets))
            for b in bullets:
                if b.shoot:
                    #print('Shoot=True')
                    if not open_menu and not gameover:
                        b.move()
                    if b.is_bullet:
                        b.image = b.bullet_image
                        #b.left =b.rect.left
                        b.draw()
                        #screen.blit(b.bullet_image, b.rect)
                    else:
                        b.image = b.firebullet_images[b.index_image]
                        b.draw()
                        #screen.blit(b.firebullet_images[b.index_image], b.rect)
                else:
                    pass
                    #print("Shoot=False?")

            # 绘制拖拽的植物图像
            if darw_pos_image:
                pos_image.draw()

            # 绘制阳光
            for s in suns:
                '''
                if s.is_supply:
                    if not open_menu and not gameover:
                        if s.gather:
                            s.move3()
                        else:
                            s.move1()
                    #screen.blit(s.images[s.index_image], s.rect1)
                    s.left = s.rect1.left
                    s.top = s.rect1.top
                    #s.image = simages[s.index_image]
                    #s.draw()
                else:
                    if not open_menu and not gameover:
                        if s.gather:
                            s.move3()
                        else:
                            s.move2()
                    screen.blit(s.images[s.index_image], s.rect2)
                    s.left = s.rect2.left
                    s.top = s.rect2.top
                '''
                if not open_menu and not gameover:
                    if s.gather:
                        s.move3()
                    else:
                        if s.is_supply:
                            s.move1()
                        else:
                            s.move2()
                s.image = s.images[s.index_image]
                s.draw()
                if s.get_position:
                    suns.remove(s)
                    sun_num += 25
            # 绘制僵尸大波袭来warn
            if large_warn_time >= 0 and large_coming:
                largewave_image.draw()
                #screen.blit(largewave_image, largewave_rect)

            # 绘制游戏结束画面
            if open_quit_window:
                quit_window_image.draw()
                quit_image.draw()
                #screen.blit(quit_window_image, quit_window_rect)
                #screen.blit(quit_image, quit_rect)
            elif bg_image.left == 0:
                music.stop()
                #screen.blit(zombiewon_image, zombiewon_rect)
                zombiewon_image.draw()
                if open_sound and not play_gameover_sound:
                    #gameover_sound.play()
                    sounds.gameover.play()
                    play_gameover_sound = True
        # 绘制阳光数量
            if not gameover:
                if seedbank.position:
                    screen.draw.text(str(sun_num), (59, 63), fontname="corisandebold.otf", fontsize=19, color=(0,0,0))

        # 绘制菜单界面
    if not gameover:
        if start_ready:
            button_image.draw()
            #screen.blit(button_image, button_rect)
        if open_menu:
            menu_image.draw()
            #screen.blit(menu_image, menu_rect)
            if start_ready:
                quitgame_image.draw()
                #screen.blit(quitgame_image, quitgame_rect)
            #screen.blit(resume_image, resume_rect)
            #screen.blit(check_box_image, check_box_rect1)
            #screen.blit(check_box_image, check_box_rect2)
            resume_image.draw()
            check_box_image1.draw()
            check_box_image2.draw()
            if open_sound:
                tick_image1.draw()
                #screen.blit(tick_image, tick_rect1)
            if open_music:
                #screen.blit(tick_image, tick_rect2)
                tick_image2.draw()
    
pgzrun.go()
