import arcade
import random

WIDTH = 300
HEIGHT = 500

# all possible x values for obstacles
x_pos = [37.5, 112.5, 187.5, 262.5]

# randomly selecting x_vales for obstacles
x_pos_ball = x_pos[(random.randrange(len(x_pos)))]
y_pos_ball = 500
ball_diameter = 15

x_pos_rect = x_pos[(random.randrange(len(x_pos)))]
y_pos_rect = 500
rect_width = 30

# player positions
left_car = 37.5
right_car = 262.5
car_width = 40

# score counter
score = 0


def on_update(delta_time):
    global y_pos_ball, y_pos_rect
    global x_pos_rect, x_pos_ball
    global score

    # makes the obstacles fall and reset once at bottom
    if x_pos_ball == x_pos_rect and (y_pos_ball + 30 == y_pos_rect or y_pos_ball + 30 == y_pos_rect):
        x_pos_rect = x_pos[(random.randrange(len(x_pos)))]

    y_pos_ball -= 2.5
    if y_pos_ball < 0:
        x_pos_ball = x_pos[(random.randrange(len(x_pos)))]
        y_pos_ball = 500
        score = 0

    y_pos_rect -= 2.5
    if y_pos_rect < 0:
        x_pos_rect = x_pos[(random.randrange(len(x_pos)))]
        y_pos_rect = 500

    # collision
    if (x_pos_rect == left_car or x_pos_rect == right_car) and (y_pos_rect - 30) == 45:
        x_pos_rect = x_pos[(random.randrange(len(x_pos)))]
        y_pos_rect = 500
        score = 0

    if (x_pos_ball == left_car or x_pos_ball == right_car) and (y_pos_ball - 7.5) == 45:
        x_pos_ball = x_pos[(random.randrange(len(x_pos)))]
        y_pos_ball = 500
        score += 1



def car():
    # drawing the cars
    arcade.draw_rectangle_filled(left_car, 45, car_width, car_width, arcade.color.BLUE)
    arcade.draw_rectangle_filled(right_car, 45, car_width, car_width, arcade.color.RED)


def obstacles():
    arcade.draw_ellipse_filled(x_pos_ball, y_pos_ball, ball_diameter, ball_diameter, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x_pos_rect, y_pos_rect, rect_width, rect_width, arcade.color.BLACK)


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
