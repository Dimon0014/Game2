import random

import arcade as arcad


class MyGame(arcad.Window):
   def on_draw(self):
       arcad.start_render()
       arcad.draw_text('Hello', 100, 100, arcad.color.WHITE)




def main():
    MyGame(600,600,'My Game_game')
    arcad.run()

if __name__ == '__main__':
    main()
