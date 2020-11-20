import pygame
class Bubble(pygame.sprite.Sprite):
    def __init__(self,canvas,pos, radius,number):
        super().__init__()
        #一個pygame物件
        self.pygame = pygame
        #畫布(物件繪製在哪邊)
        self.canvas = canvas
        #設置圓心位置
        self.pos = pos
        #球的半徑
        self.radius = radius
        #球的顏色
        self.color = (80,180,180)
        self.outColor = (38,57,117)
        #實/空 心
        self.visible = True
        self.number = number
        self.numberFont = pygame.font.SysFont("None", 28)
        self.numberText = self.numberFont.render(str(number),True, (255,255,255))
        self.outSide = self.pygame.draw.circle(self.canvas, self.outColor, self.pos, self.radius)
        self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius - 3)
    def setX(self,x):
        self.pos[0] = x
    def setY(self,y):
        self.pos[1] = y
    def getPos(self):
        return self.pos
    def update(self):
        if(self.visible):
            self.outSide = self.pygame.draw.circle(self.canvas, self.outColor, self.pos, self.radius)
            self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos , self.radius - 3)
            self.numberText = self.numberFont.render(str(self.number),True, (255,255,255))
            self.canvas.blit(self.numberText,(self.pos[0]-self.numberText.get_width()/2,self.pos[1]-self.numberText.get_height()/2))
    def remove(self):
        if(self.visible):
            self.visible = False
            # self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)
class Button(object):
    def __init__(self,canvas,rect,msg):
        self.pygame = pygame
        self.canvas = canvas
        self.rect = rect
        self.msg = msg
        self.color = (255,255,255)
        self.msgFont = pygame.font.SysFont("None", 28)
        self.msgText = self.msgFont.render(msg,True, (0,0,0))
        self.visible = False
    def setVisible(self, visible):
        self.visible = visible
    def getRect(self):
        return self.rect
    def update(self):
        if(self.visible):
            self.pygame.draw.rect(self.canvas, self.color, self.rect)
            self.canvas.blit(self.msgText,(self.rect[0]+self.rect[2]/2-self.msgText.get_width()/2,self.rect[1]+self.rect[3]/2-self.msgText.get_height()/2))
