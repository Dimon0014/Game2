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

       self.coin_list = arcad.SpriteList()
       for i in range(50):
          coin = arcad.Sprite('coin.png', 0.15)
          coin.center_x = random.randrange(600)
          coin.center_y = random.randrange(600)
          self.all_sprites_list.append(coin) # это все в цикле делается, в том числе
                                             # coin объявляется
          self.coin_list.append(coin)
   def on_draw(self):
       arcad.start_render()
       output = f'Score: {self.score:02d}'
       arcad.draw_text(output, 100, 100, arcad.color.WHITE)
       self.all_sprites_list.draw()
   def update(self, delta_time):

       self.all_sprites_list.update()
       hit_list = arcad.check_for_collision_with_list(
           self.player_sprite,
           self.coin_list
       )
       for coin in hit_list:
           coin.kill()
           self.score += 1
   def on_mouse_motion(self, x, y, dx, dy):
       self.player_sprite.center_x = x
       self.player_sprite.center_y = y

def main():
    MyGame(600,600,'My Game_game')
    arcad.run()

if __name__ == '__main__':
    main()
