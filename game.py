import arcade as arcad


class MyGame(arcad.Window):

   def __init__(self, width, height, title):
       super().__init__(width, height, title)
       arcad.set_background_color(arcad.color.AMAZON)
       self.score = 0
   def on_draw(self):
       arcad.start_render()
       output = f'Score: {self.score:02d}'
       arcad.draw_text(output, 100, 100, arcad.color.WHITE)




def main():
    MyGame(600,600,'My Game_game')
    arcad.run()

if __name__ == '__main__':
    main()
