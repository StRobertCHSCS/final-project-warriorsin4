import arcade
import random

WIDTH = 300
HEIGHT = 500

# all possible x and y values for square obstacles
x_pos_square = [37.5, 112.5, 187.5, 262.5]
y_pos_square = [700, 550, 600, 810]

# Create a list that stores the falling squares
x_pos_store_square = []
y_pos_store_square = []

for i in range(10):
    x = random.randrange(len(x_pos_square))
    y = random.randrange(len(y_pos_square))

    x_pos_store_square.append(x)
    y_pos_store_square.append(y)

#  all possible x and y values for circle obstacles
x_pos_circle = [37.5, 112.5, 187.5, 262.5]
y_pos_circle = [800, 700, 500, 900]

# Create a list that stores the falling circles
x_pos_store_circle = []
y_pos_store_circle = []

for i in range(10):
    x = random.randrange(len(x_pos_circle))
    y = random.randrange(len(y_pos_circle))

    x_pos_store_circle.append(x)
    y_pos_store_circle.append(y)

# player positions
left_car = 37.5
right_car = 262.5
car_width = 40

# score counter
score = 0
ball_diameter = 15
rect_width = 30


def on_update(delta_time):
    global y_pos_square, x_pos_square
    # makes the obstacles fall and reset once at bottom
    for i in range(len(y_pos_square)):
        y_pos_square[i] -= 2.5

        if y_pos_square[i] < 0:
            y_pos_square[i] = random.randrange(HEIGHT, HEIGHT + 50)
            x_pos_square[i] = random.randrange(0, WIDTH)

    for i in range(len(y_pos_circle)):
        y_pos_circle[i] -= 2.5

        if y_pos_circle[i] < 0:
            y_pos_circle[i] = random.randrange(HEIGHT, HEIGHT + 50)
            x_pos_circle[i] = random.randrange(0, WIDTH)

def car():
    # drawing the cars
    arcade.draw_rectangle_filled(left_car, 45, car_width, car_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_car, 45, car_width, car_width, arcade.color.RED)


def obstacles():
    for x, y in zip(x_pos_square, y_pos_square):
        arcade.draw_rectangle_filled(x, y, rect_width, rect_width, arcade.color.BLACK)
    for x, y in zip(x_pos_circle, y_pos_circle):
        arcade.draw_ellipse_filled(x, y, ball_diameter, ball_diameter, arcade.color.BLUE)


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

    # drawing the obstacles
    obstacles()

    arcade.draw_text("Score: " + str(score), 262.5, 400, arcade.color.BLACK, 12, 12)

    car()


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
