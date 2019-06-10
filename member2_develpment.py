import arcade
import random

WIDTH = 300
HEIGHT = 500

# all possible x values for obstacles
x_pos_square = [37.5, 112.5, 187.5, 262.5]
y_pos_square = [900,  620, 560, 800]

x_pos_circle = [37.5, 112.5, 187.5, 262.5]
y_pos_circle = [550,  800, 700, 600]

# randomly selecting x_vales for obstacles

ball_diameter = 15

rect_width = 30

# player positions
left_car = 37.5
right_car = 262.5
car_width = 40

# score counter
score = 0

x_square_storing = []
y_square_storing = []

for i in range(10):
    # generate random x and y values
    x = x_pos_square[random.randrange(len(x_pos_square))]
    y = y_pos_square[random.randrange(len(y_pos_square))]

    # append the x and y values to the appropriate list
    x_square_storing.append(x)
    y_square_storing.append(y)

x_circle_storing = []
y_circle_storing = []

for i in range(10):
    # generate random x and y values
    x = x_pos_circle[random.randrange(len(x_pos_circle))]
    y = y_pos_circle[random.randrange(len(y_pos_circle))]

    # append the x and y values to the appropriate list
    x_circle_storing.append(x)
    y_circle_storing.append(y)

print(x_square_storing)

def on_update(delta_time):
    global y_pos_ball, y_pos_rect
    global x_pos_rect, x_pos_ball
    global score

    for index in range(len(y_square_storing)):
        y_square_storing[index] -= 2.5

        # make a new list
        if y_square_storing[index] < 0:
            y_square_storing[index] = random.randrange(HEIGHT, HEIGHT+50)
            x_square_storing[index] = x_pos_square[random.randrange(len(x_pos_square))]

    for index in range(len(y_circle_storing)):
        y_circle_storing[index] -= 2.5

        # make a new list
        if y_circle_storing[index] < 0:
            y_circle_storing[index] = random.randrange(HEIGHT, HEIGHT + 50)
            x_circle_storing[index] = x_pos_circle[random.randrange(len(x_pos_circle))]


def car():
    # drawing the cars
    arcade.draw_rectangle_filled(left_car, 45, car_width, car_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_car, 45, car_width, car_width, arcade.color.RED)


def obstacles():
    for x, y in zip(x_square_storing, y_square_storing):
        arcade.draw_rectangle_filled(x, y, rect_width, rect_width, arcade.color.BLUE)
    for x, y in zip(x_circle_storing, y_circle_storing):
        arcade.draw_ellipse_filled(x, y, ball_diameter, ball_diameter, arcade.color.RED)

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
