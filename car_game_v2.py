import arcade
import random

WIDTH = 400
HEIGHT = 500

car_width = 30
left_car = 35
right_car = 335

acceleration = 0
velocity = 0


def on_key_press(key, modifiers):
    global left_car, acceleration, velocity, height, gravity

    if key == arcade.key.S:

        acceleration += 1


def on_key_release(key, modifiers):
    pass



def on_mouse_press(x, y, button, modifiers):
    pass


def game_screen():
    # draw outline of game
    for i in range(WIDTH):
        if i % 100 == 0:
            arcade.draw_line(i, 0, i, HEIGHT, arcade.color.BLACK, 5)
        if i == 200:
            arcade.draw_line(i, 0, i, HEIGHT, arcade.color.BLACK, 10)

    arcade.draw_xywh_rectangle_outline(left_car, 50, car_width, car_width, arcade.color.BLUE, 5)
    arcade.draw_xywh_rectangle_outline(right_car, 50, car_width, car_width, arcade.color.RED, 5)


def on_update(delta_time):
    global left_car, acceleration, velocity, gravity

    if left_car < 135:
        velocity += acceleration
        left_car += velocity






def on_draw():
    arcade. start_render()
    game_screen()


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)


    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
