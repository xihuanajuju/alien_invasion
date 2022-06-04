import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game) -> None:
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #对于每艘飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom #为什么不直接调用ai_game.screen.get_rect()?

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image ,self.rect)