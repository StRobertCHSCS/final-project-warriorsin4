import arcade
import random

WIDTH = 300
HEIGHT = 500

# Set a time variable
time= 0

# obstacle positions
x_pos_ball = [37.5, 112.5, 187.5, 262.5]
y_pos_ball = HEIGHT
ball_diameter = 30

x_pos_rect = [37.5, 112.5, 187.5, 262.5]
y_pos_rect = HEIGHT
rect_width = 30

# player positions
left_car = 37.5
right_car = 262.5
car_width = 40

# Obstacle positions
left_obstacle = 37.5
right_obstacle = 262.5
left_y_obstacle = 480
right_y_obstacle = 480
obstacle_width = 20


def on_update(delta_time):
    global time, left_y_obstacle, right_y_obstacle
    time += 1
    if time == 10:
        left_y_obstacle -= 40
        right_y_obstacle -= 30
        time = 0
        
def car():
    arcade.draw_rectangle_filled(left_car, 45, car_width, car_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_car, 45, car_width, car_width, arcade.color.RED)


def obstacle():
    arcade.draw_rectangle_filled(left_obstacle, left_y_obstacle, obstacle_width, obstacle_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_obstacle, right_y_obstacle, obstacle_width, obstacle_width, arcade.color.RED)


def on_key_press(key, modifiers):
    global left_car, right_car

    # left car movement controls
    if key == arcade.key.S and left_car == 37.5:
        left_car += 75
    elif key == arcade.key.S and left_car == 112.5:
        left_car -= 75

    # right car movement controls
    if key == arcade.key.DOWN and right_car == 262.5:
        right_car -= 75
    elif key == arcade.key.DOWN and right_car == 187.5:
        right_car += 75

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def on_draw():
    arcade.start_render()

    # draw outlines of track
    for x in range(WIDTH):
        if x % 75 == 0 and x != 150:
            arcade.draw_line(x, 0, x, HEIGHT, arcade.color.BLACK, 5)
        elif x == 150:
            arcade.draw_line(x, 0, x, HEIGHT, arcade.color.BLACK, 15)

    car()
    obstacle()

def setup():
    arcade.open_window(WIDTH, HEIGHT, "2 Cars")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)
    obstacle()
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
