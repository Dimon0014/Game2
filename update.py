"""
Sprite Change Coins

This shows how you can change a sprite once it is hit, rather than eliminate it.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_change_coins
"""

import random
import arcade
import os

SPRITE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Collectable(arcade.Sprite):
    """ This class represents something the player collects. """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coin has been collected.
        self.changed = False


class MyGame(arcade.Window):
    """
    Main application class.a
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        # Create the coin instance
        self.coin = Collectable("images/coin_01.png", SPRITE_SCALING)
        self.coin.width = 30
        self.coin.height = 30
        self.coin.center_x = 150
        self.coin.center_y = 160
        self.all_sprites_list.append(self.coin)
        #self.coin_list.append(coin)
        # for i in range(50):
        #
        #     # Create the coin instance
        #     coin = Collectable("images/coin_01.png", SPRITE_SCALING)
        #     coin.width = 30
        #     coin.height = 30
        #
        #     # Position the coin
        #     coin.center_x = random.randrange(SCREEN_WIDTH)
        #     coin.center_y = random.randrange(SCREEN_HEIGHT)
        #
        #     # Add the coin to the lists
        #     self.all_sprites_list.append(coin)
        #     self.coin_list.append(coin)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()
        #
        # # Generate a list of all sprites that collided with the player.
        # hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        #
        # # Loop through each colliding sprite, change it, and add to the score.
        # for coin in self.all_sprites_list:
        # #     # Have we collected this?
        #         if not coin.changed:
                        # No? Then do so
        self. coin.texture = arcade.load_texture("images/bumper.png")
        self.coin.width = 30
        self.coin.height = 30
        #                 changed = True
        #                 width = 30
        #                 height = 30
        # #self.score += 1


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()