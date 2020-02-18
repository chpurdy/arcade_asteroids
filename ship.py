from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import arcade
import math

class Ship:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.heading = heading # degrees
        self.rotation = 0
        self.lasers = []
        
    def draw(self):
        top = arcade.Point(self.x,self.y+10)
        left = arcade.Point(self.x-10, self.y-10)
        right = arcade.Point(self.x+10, self.y-10)
        
        top = arcade.rotate_point(top[0],top[1],self.x,self.y,self.heading)
        right = arcade.rotate_point(right[0],right[1],self.x,self.y,self.heading)
        left = arcade.rotate_point(left[0],left[1],self.x,self.y,self.heading)
        arcade.draw_triangle_outline(top[0],top[1],
                                     right[0],right[1],
                                     left[0],left[1],
                                     arcade.color.WHITE)
        for laser in self.lasers:
            laser.draw()
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.heading += self.rotation
        if self.x < 0:
            self.x = SCREEN_WIDTH
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        if self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y > SCREEN_HEIGHT:
            self.y = 0
        for laser in self.lasers:
            if laser.on_screen():
                laser.update()
            else:
                self.lasers.remove(laser)
    
    def rotate(self,direction):
        if direction == 'LEFT':
            self.rotation = 10
        if direction == 'RIGHT':
            self.rotation = -10
        
    def move(self, direction):
        rad = math.radians(self.heading-90)
        if direction == 'FORWARD':
            self.dx -= math.cos(rad)
            self.dy -= math.sin(rad)
        if direction == 'BACKWARD':
            self.dx += math.cos(rad)
            self.dy += math.sin(rad)
    
    def shoot(self):
        self.lasers.append(Laser(self.x, self.y, self.heading))
        
class Laser:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = math.radians(heading+90)
        self.length = 10
        self.color = arcade.color.WHITE
        self.speed = 10
        
         
    
    def draw(self):
        arcade.draw_line(self.x, self.y, self.x+self.length*math.cos(self.heading), self.y+self.length*math.sin(self.heading),self.color)
    
    def update(self):
        self.x += self.speed * math.cos(self.heading)
        self.y += self.speed * math.sin(self.heading)
        
    def on_screen(self):
        return self.x > 0 and self.x < SCREEN_WIDTH and self.y > 0 and self.y < SCREEN_HEIGHT