import arcade
import random

WIDTH = 300
HEIGHT = 500

# player positions
left_car = 37.5
right_car = 262.5
car_width = 40

# score counter
score = 0
ball_radius = 15
rect_width = 30

# empty list storing x and y values of obstacles
x_circle = []
y_circle = []

x_square = []
y_square = []

# all possible x values of obstacles.
x_pos = [37.5, 112.5, 187.5, 262.5]

for _ in range(2):
    # generate random x and y values
    x = x_pos[random.randrange(len(x_pos))]
    y = random.randrange(HEIGHT, HEIGHT*2)

    square_x = x_pos[random.randrange(len(x_pos))]
    square_y = random.randrange(HEIGHT, HEIGHT*2)

    # append the x and y values to the appropriate list
    x_circle.append(x)
    y_circle.append(y)

    x_square.append(square_x)
    y_square.append(square_y)

def on_update(delta_time):
    global score

    for index in range(len(y_circle)):
        y_circle[index] -= 2.5
        y_square[index] -= 2.5

        if y_circle[index] < 0:
            y_circle[index] = random.randrange(HEIGHT, HEIGHT+50)
            x_circle[index] = x_pos[random.randrange(len(x_pos))]

        if y_square[index] < 0:
            y_square[index] = random.randrange(HEIGHT, HEIGHT+50)
            x_square[index] = x_pos[random.randrange(len(x_pos))]

        if y_circle[index] < 45 and x_circle[index] == left_car:
            y_circle[index] = random.randrange(HEIGHT, HEIGHT+50)
            x_circle[index] = x_pos[random.randrange(len(x_pos))]
            score += 1

        if y_circle[index] < 45 and x_circle[index] == right_car:
            y_circle[index] = random.randrange(HEIGHT, HEIGHT+50)
            x_circle[index] = x_pos[random.randrange(len(x_pos))]
            score += 1



def car():
    # drawing the cars
    arcade.draw_rectangle_filled(left_car, 45, car_width, car_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_car, 45, car_width, car_width, arcade.color.RED)


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

    for x, y in zip(x_circle, y_circle):
        arcade.draw_circle_filled(x, y, ball_radius, arcade.color.BLUE)

    for f, t in zip(x_square, y_square):
        arcade.draw_rectangle_filled(f, t, rect_width, rect_width, arcade.color.RED)

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
