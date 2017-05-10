import arcade as arcad
import random
import math

class MyGame(arcad.Window):

   def __init__(self, width, height, title):
       super().__init__(width, height, title)
       arcad.set_background_color(arcad.color.AMAZON)
       self.score = 0
       self.all_sprites_list = arcad.SpriteList()
       self.player_sprite = arcad.Sprite('character2.png', 0.7)
       self.player_sprite.center_x = 50
       self.player_sprite.center_y = 50
       self.all_sprites_list.append(self.player_sprite)
   def on_draw(self):
       arcad.start_render()
       output = f'Score: {self.score:02d}'
       arcad.draw_text(output, 100, 100, arcad.color.WHITE)
       self.all_sprites_list.draw()
   def update(self, delta_time):
       self.score += 1
       self.all_sprites_list.update()

def main():
    MyGame(600,600,'My Game_game')
    arcad.run()

if __name__ == '__main__':
    main()
