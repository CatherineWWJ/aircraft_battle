import random
import pygame

# 定义常量，所有字母都要大写，单词之间用下划线连接
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT # 创建敌机的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT+1 # 创建英雄飞机发射子弹的定时器常量

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1):
        # 调用父类的初始化方法
        super().__init__()

        # 图像+位置+速度
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向上移动
        self.rect.y += self.speed

# 背景类
# 父类提供的方法不能满足子类的需求，针对特有需求，重写父类方法，进行扩展
class Background(GameSprite):
    def __init__(self, is_alt = False):
        # is_alt为True则表示该背景为交替背景图
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.kill() # 将精灵从所有精灵组中移除并销毁

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄飞机左右移动
        self.rect.x += self.speed
        if self.rect.x<0:
            self.rect.x = 0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.top - i*20
            self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()