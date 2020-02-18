import arcade
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ship import Ship, Laser
from asteroid import Asteroid
from random import randint


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Asteroids')
        
    def setup(self):
        self.ship = Ship(self.width/2,self.height/2,0)
        self.asteroids = []
        for i in range(5):
            r = 30
            x = randint(r,SCREEN_WIDTH - r)
            y = randint(r,SCREEN_HEIGHT - r)
            xv = randint(-5,5)
            yv = randint(-5,5)
            self.asteroids.append(Asteroid(x,y,r,xv,yv))
    
    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        
    def on_update(self, delta_time):
        self.ship.update()
        for asteroid in self.asteroids:
            asteroid.update()
    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.rotate('LEFT')
        
        if key == arcade.key.RIGHT:
            self.ship.rotate('RIGHT')
            
        if key == arcade.key.UP:
            self.ship.move('FORWARD')
        
        if key == arcade.key.DOWN:
            self.ship.move('BACKWARD')
            
        if key == arcade.key.SPACE:
            self.ship.shoot()
    
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.rotation = 0
        
        if key == arcade.key.RIGHT:
            self.ship.rotation = 0
    
    
def main():
    game = Game()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()