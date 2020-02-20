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
        self.lives = []
        self.game_over = False
        for i in range(3):
            self.lives.append(Ship(SCREEN_WIDTH-150+i*50, SCREEN_HEIGHT-50,0,arcade.color.RED,arcade.color.BLUE))
        self.score = 0
        self.ship = Ship(self.width/2,self.height/2,0,arcade.color.RED,arcade.color.BLUE)
        self.asteroids = []
        for i in range(5):
            r = 30
            x = randint(r,SCREEN_WIDTH - r)
            y = randint(r,SCREEN_HEIGHT - r)
            xv = randint(-5,5)
            yv = randint(-5,5)
            bc = (randint(0,255),randint(0,255),randint(0,255))
            ic = (255-bc[0],255-bc[1],255-bc[2])
            self.asteroids.append(Asteroid(x,y,r,xv,yv,bc,ic))
    
    def on_draw(self):
        
        arcade.start_render()
        if not self.game_over:
            for life in self.lives:
                life.draw()
            arcade.draw_text(f"Score: {self.score}",SCREEN_WIDTH-100,SCREEN_HEIGHT-20,arcade.color.WHITE,12)
            self.ship.draw()
            for asteroid in self.asteroids:
                if self.ship.check_collide(asteroid):
                    if len(self.lives) > 0:
                        self.lives.pop(0)
                        self.ship.reset()
                    else:
                        self.game_over = True
                asteroid.draw()
        else:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50, arcade.color.RED, 30,anchor_x="center")
            arcade.draw_text(f"Final Score: {self.score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.RED,30,anchor_x="center")
            arcade.draw_text("Press 'Q' to Quit or 'R' to Restart",SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50, arcade.color.RED, 30, anchor_x="center")
        
    def on_update(self, delta_time):
        if not self.game_over:
            self.ship.update()
            self.score += self.ship.check_hit(self.asteroids)
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
            
        if self.game_over:
            if key == arcade.key.Q:
                arcade.close_window()
            
            if key == arcade.key.R:
                self.setup()
    
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