import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 800, 600  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
RED = 200, 0, 0
BOX1 = pygame.Rect((580, 399), (24, 24))
BOX2= pygame.Rect((601, 330), (166, 144))
#580.0 399.0 24 24
#601.0 330.0 166 144
while True:  # 死循环确保窗口一直显示

    pygame.draw.rect(screen, RED, BOX1 ) 
    pygame.draw.rect(screen, RED, BOX2 ) 
    pygame.display.update()
    #pygame.draw.rect(BOX, RED)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

#pygame.quit()  # 退出pygame
