import arcade as arcad

class MyGame(arcad.Window):
   def on_draw(self):
       arcad.start_render()
       arcad.draw_text('Hello', 100, 100, arcad.color.WHITE)

       ("""arcade.open_window(600, 600, 'My Game' )
       arcade.finish_render()""")


def main():
    MyGame(600,600,'My Game')
    arcad.run()

if __name__ == '__main__':
    main()
