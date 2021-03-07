import pygame #是一个用来创建游戏的库
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()

    def move(self):
        if self.y < 0:#如果子弹离开了屏幕范围
            mouseX,mouseY = pygame.mouse.get_pos()
            self.x = mouseX - self.image.get_width()/2
            self.y = mouseY - self.image.get_height()/2
        else:
            self.y -= 5

pygame.init() #初始化pygame

screen = pygame.display.set_mode((700,669),0,32) #创建了一个窗口大小，大小为600x170像素
pygame.display.set_caption("Hello,Pygame~!") #设置窗口标题
background = pygame.image.load("1.jpeg").convert()
player = pygame.image.load('21.png')
bullet = Bullet()
#http://koutu.fjdaze.com/
while True:
    #让程序进入重复循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
    bullet.move()
    screen.blit(bullet.image,(bullet.x,bullet.y))
    # 加载背景图
    x,y = pygame.mouse.get_pos()
    x -= player.get_width()/2
    y -= player.get_height()/2
    screen.blit(player, (x,y))
    pygame.display.update()
