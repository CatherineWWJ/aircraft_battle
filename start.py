import pygame
from plane_sprites import *

pygame.init()

# 创建主窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))

# 统一更新界面
pygame.display.update()

# 时钟对象
clock = pygame.time.Clock()

# 记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)

# 创建敌机精灵+精灵组
enemy = GameSprite("./images/enemy1.png")
enemy_group = pygame.sprite.Group(enemy)

while True:
    # 可以指定循环体内部代码执行频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 卸载所有的模块+退出游戏（直接终止当前正在执行的程序）
            pygame.quit()
            exit()

    hero_rect.y -= 1

    if hero_rect.y<=0-126:
        hero_rect.y = 700

    # 重新绘制图片
    screen.blit(bg, (0,0))
    screen.blit(hero, hero_rect)

    # 让精灵组更新位置并绘制
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()


pygame.quit()
