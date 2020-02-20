from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ship import Ship, Laser

import arcade

class Asteroid:
    def __init__(self, x, y, r, x_vel, y_vel,border_color=arcade.color.WHITE,inner_color=arcade.color.BLACK):
        self.x = x
        self.y = y
        self.r = r
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.border_color = border_color
        self.inner_color = inner_color
    
    def draw(self):
        
        if self.x + self.r > SCREEN_WIDTH:
            arcade.draw_circle_filled(self.x-SCREEN_WIDTH, self.y, self.r, self.inner_color)
            arcade.draw_circle_outline(self.x-SCREEN_WIDTH, self.y, self.r, self.border_color)
        
        if self.x - self.r < 0:
            arcade.draw_circle_filled(SCREEN_WIDTH+self.x, self.y, self.r, self.inner_color)
            arcade.draw_circle_outline(SCREEN_WIDTH+self.x, self.y, self.r, self.border_color)
        
        if self.y + self.r > SCREEN_HEIGHT:
            arcade.draw_circle_filled(self.x, self.y-SCREEN_HEIGHT, self.r, self.inner_color)
            arcade.draw_circle_outline(self.x, self.y-SCREEN_HEIGHT, self.r, self.border_color)
        
        if self.y - self.r < 0:
          
            arcade.draw_circle_filled(self.x, SCREEN_HEIGHT+self.y, self.r, self.inner_color)             
            arcade.draw_circle_outline(self.x, SCREEN_HEIGHT+self.y, self.r, self.border_color)
        
        arcade.draw_circle_filled(self.x,self.y,self.r,self.inner_color)
        arcade.draw_circle_outline(self.x,self.y,self.r,self.border_color)
    
    def split(self):
        if self.r > 5:
            left = Asteroid(self.x, self.y, self.r//2, -self.x_vel, self.y_vel,self.border_color,self.inner_color)
            right = Asteroid(self.x, self.y, self.r//2, self.x_vel, -self.y_vel,self.inner_color,self.border_color)
            return [left, right]
    
    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
        
        if self.x - self.r > SCREEN_WIDTH:
            self.x = self.r
            
        if self.x + self.r < 0:
            self.x = SCREEN_WIDTH - self.r
        
        if self.y - self.r > SCREEN_HEIGHT:
            self.y = self.r
            
        if self.y + self.r < 0:
            self.y = SCREEN_HEIGHT - self.r
            
    
    

