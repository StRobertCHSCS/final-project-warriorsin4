import arcade
import random

WIDTH = 400
HEIGHT = 500

car_width = 30
left_car = 50
left_car_tilt = 0
right_car = 350
right_car_tilt = 0

acceleration = 0
velocity = 0

turn_direction_left = False


def on_key_press(key, modifiers):
    global acceleration, velocity, turn_direction_left, left_car_tilt

# when button is pressed, start accelerating
    if key == arcade.key.S and turn_direction_left is False:
        acceleration += 2
        left_car_tilt = -10
        turn_direction_left = True

    elif key == arcade.key.S and turn_direction_left is True:
        acceleration -= 2
        left_car_tilt = 10
        turn_direction_left = False


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

    arcade.draw_rectangle_outline(left_car, 50, car_width, car_width, arcade.color.BLUE, 5, left_car_tilt)
    arcade.draw_rectangle_outline(right_car, 50, car_width, car_width, arcade.color.RED, 5, right_car_tilt)


def on_update(delta_time):
    global left_car, acceleration, velocity, left_car_tilt

    velocity += acceleration
    left_car += velocity

    if left_car >= 150:
        velocity = 0
        acceleration = 0
        left_car_tilt = 0
        left_car = 150

    elif left_car <= 50:
        velocity = 0
        acceleration = 0
        left_car_tilt = 0
        left_car = 50


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
