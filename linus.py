import pygame

"""新加一行"""
class Linus:
    """管理linus的类"""

    def __init__(self, ai_game) -> None:
        """加载linus的图片并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载linus图片并获取其矩形
        self.image = pygame.image.load("./images/linus.bmp")
        self.rect = self.image.get_rect()

        #将linus放置到屏幕正中央
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """在指定位置绘制linus"""
        self.screen.blit(self.image, self.rect)