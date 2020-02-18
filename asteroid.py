from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ship import Ship, Laser

import arcade

class Asteroid:
    def __init__(self, x, y, r, x_vel, y_vel):
        self.x = x
        self.y = y
        self.r = r
        self.x_vel = x_vel
        self.y_vel = y_vel
    
    def draw(self):
        if self.x + self.r > SCREEN_WIDTH:
            arcade.draw_circle_outline(self.x,self.y,self.r,arcade.color.WHITE)
            arcade.draw_circle_outline(self.x-SCREEN_WIDTH, self.y, self.r, arcade.color.WHITE)
        
        elif self.x - self.r < 0:
            arcade.draw_circle_outline(self.x,self.y,self.r,arcade.color.WHITE)
            arcade.draw_circle_outline(SCREEN_WIDTH+self.x, self.y, self.r, arcade.color.WHITE)
        
        elif self.y + self.r > SCREEN_HEIGHT:
            arcade.draw_circle_outline(self.x,self.y,self.r,arcade.color.WHITE)
            arcade.draw_circle_outline(self.x, self.y-SCREEN_HEIGHT, self.r, arcade.color.WHITE)
        
        
        ## THIS IS BROKEN WHY?
        elif self.y - self.r < 0:
            arcade.draw_circle_outline(self.x,self.y,self.r,arcade.color.WHITE)
            arcade.draw_circle_outline(self.x, self.SCREEN_HEIGHT+self.y, self.r, arcade.color.WHITE)
        
        else:
            arcade.draw_circle_outline(self.x,self.y,self.r,arcade.color.WHITE)
    
    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
        if self.x - self.r > SCREEN_WIDTH:
            self.x = self.r
            
        elif self.x + self.r < 0:
            self.x = SCREEN_WIDTH - self.r
        
        if self.y - self.r > SCREEN_HEIGHT:
            self.y = self.r
            
        elif self.y + self.r < 0:
            self.y = SCREEN_HEIGHT - self.r
            
    
    

