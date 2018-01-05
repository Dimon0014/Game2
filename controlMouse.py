"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50
SPRITE_SCALING = 0.7
class Collectable(arcade.Sprite):
    """ This class represents something the player collects. """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coin has been collected.
        # Position
        self.x = 250
        self.y = 260
        self.changed = False
        self.center_x = self.x
        self.center_y = self.y
    def get_x(self):
            return self.x

    def get_y(self):
            return self.y

    # def update(self):
    #         self.all_sprites_list.update()




class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.

        self.texture_yel = arcade.load_texture("images/yel_butn.png", scale=SPRITE_SCALING)
        self.texture_red = arcade.load_texture("images/red_butn.png", scale=SPRITE_SCALING)

        # By default, face right.
        self.texture = self.texture_yel
class Buttn():
    def __init__(self, x, y, width, height):

        # Position
        self.x = 250
        self.y = 260

        # Size and rotation
        self.width = width
        self.height = height
        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = Collectable("images/yel_butn.png", SPRITE_SCALING)
        self.player_sprite.center_x = self.x
        self.player_sprite.center_y = self.y
        self.all_sprites_list.append(self.player_sprite)


    def draw(self):
        """ Draw our rectangle """
        self.all_sprites_list.draw()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.all_sprites_list.update()
class Rectangle:
    """ Class to represent a rectangle on the screen """

    def __init__(self, x, y, width, height, angle, color):
        """ Initialize our rectangle variables """

        # Position
        self.x = 150
        self.y = 160

        # Size and rotation
        self.width = width
        self.height = height
        self.angle = angle

        # Color
        self.color = color

    def draw(self):
        """ Draw our rectangle """
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)
    def get_x(self):
        return  self.x
    def get_y(self):
        return self.y
class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard control")
        self.player = None
        self.left_down = False
        self.vkl = True
    def setup(self):
        """ Set up the game and initialize the variables. """
        width = RECT_WIDTH
        height = RECT_HEIGHT
        x = 0
        y = RECT_HEIGHT
        angle = 0
        color = arcade.color.WHITE
        #self.player = Rectangle(x, y, width, height, angle, color) # назначение плейру прямоугольника
        self.player = Collectable("images/yel_butn.png", SPRITE_SCALING)
        self.left_down = False

    def update(self, dt): # обработка клика,
                   # dt (float):	Time interval since the last time the function was called.
        """ Move everything """
        self.player.update()
        if self.left_down:
          while self.vkl:
           print("klik po knopke")

           self.player.texture = arcade.load_texture("images/red_butn.png")
           self.player.width = 70
           self.player.height = 70
           self.vkl = False
           # self.player.angle += 2

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        #output = f'Score: {self.score:02d}'
        arcade.draw_text('output', 100, 100, arcade.color.WHITE)
        self.player.draw()

    # def on_mouse_motion(self, x, y, dx, dy):
    #     """
    #     Called whenever the mouse moves.
    #     """
    #     self.player.x = x
    #     self.player.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button. в любом месте экрана
        """
        print(button) # печатает номер кнопки мыши если один  то левая кнопка
        x_player =  self.player.get_x()
        y_player = self.player.get_y()
        if (x<(x_player+30) and x >(x_player-30)) and (y<(y_player+30) and y >(y_player-30)):
         if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = True

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.left_down = False
            self.vkl = True

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()