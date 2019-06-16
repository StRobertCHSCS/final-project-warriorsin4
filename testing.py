import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_OBSTACLE = 0.2
OBSTACLE_COUNT = 4

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
SCREEN_TITLE = "CAR GAME"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """



    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        for i in range(SCREEN_WIDTH):
            if i % 100 == 0:
                arcade.draw_line(i, 0, i, SCREEN_HEIGHT, arcade.color.BLACK, 5)
            if i == 200:
                arcade.draw_line(i, 0, i, SCREEN_HEIGHT, arcade.color.BLACK, 10)

    def update(self, delta_time):
        """ Movement and game logic """




def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()