import pygame

pygame.init()     #需要初始化

text = u"Jiaxin"        #将文本以unicode编码格式存储

# 用 pygame.font.get_fonts() 查询可用字体
# my_font = pygame.font.SysFont("arial",16) # 使用系统字体
font = pygame.font.Font(".\my_font\HYXingQiuTiJ.ttf", 50)  #设置字体

# render(text, antialias, color, background=None)
# ftext = font.render(text, True, (255, 255, 255, 0.3),(0,0,0))   #渲染字体
ftext = font.render(text, True, (0, 0, 0, 0.3))

pygame.image.save(ftext, ".\pic\jiaxin.png")   #存储图像
