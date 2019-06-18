import arcade
import random
import math

WIDTH = 400
HEIGHT = 500

# initializing all car related variables
car_y = 50
car_width = 30
left_car = 50
left_car_tilt = 0
right_car = 350
right_car_tilt = 0

left_acceleration = 0
left_velocity = 0

right_acceleration = 0
right_velocity = 0

turn_direction_left = False
turn_direction_right = False

# initializing all obstacle related variables
ball_radius = 15
rect_width = 30

x_circle = []
y_circle = []

x_square = []
y_square = []

# all possible x values of obstacles.
x_pos = [50, 150, 250, 350]

# set variables for menu screen buttons
start_button = [100, 400, 200, 100]
help_button = [100, 150, 200, 100]
try_again_button = [200, 180, 200, 100]
main_menu_button = [200, 80, 200, 100]

for _ in range(2):
    # generate random x and y values
    x = x_pos[random.randrange(len(x_pos))]
    y = random.randrange(HEIGHT, HEIGHT*3)

    square_x = x_pos[random.randrange(len(x_pos))]
    square_y = random.randrange(HEIGHT, HEIGHT*3)

    # append the x and y values to the appropriate list
    x_circle.append(x)
    y_circle.append(y)

    x_square.append(square_x)
    y_square.append(square_y + 200)

# variable that decides which screen to display
screen_display = 0
score = 0


def on_key_press(key, modifiers):
    """

    :param key:
    :param modifiers:
    :return:
    """
    global left_acceleration, left_velocity, right_velocity, turn_direction_left, turn_direction_right, left_car_tilt,\
        right_car_tilt, right_acceleration

# when button is pressed, start accelerating. Direction of movement depends on state
# of turn_direction. if false turn certain direction, if true turn another direction
    if key == arcade.key.S and turn_direction_left is False:
        left_velocity = 0
        left_acceleration = 0
        left_acceleration += 2
        left_car_tilt = -10
        turn_direction_left = True
    elif key == arcade.key.S and turn_direction_left is True:
        left_velocity = 0
        left_acceleration = 0
        left_acceleration -= 2
        left_car_tilt = 10
        turn_direction_left = False

    if key == arcade.key.DOWN and turn_direction_right is False:
        right_velocity = 0
        right_acceleration = 0
        right_acceleration -= 2
        right_car_tilt = 10
        turn_direction_right = True
    elif key == arcade.key.DOWN and turn_direction_right is True:
        right_velocity = 0
        right_acceleration = 0
        right_acceleration += 2
        right_car_tilt = -10
        turn_direction_right = False


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    """

    :param x:
    :param y:
    :param button:
    :param modifiers:
    :return:
    """
    global screen_display

    # unpack the list
    start_button_x, start_button_y, start_button_w, start_button_h = start_button

    # Need to check all four limits of the button.
    if (x > start_button_x and x < start_button_x + start_button_w and
            y > start_button_y and y < start_button_y + start_button_h) and screen_display == 0:
        screen_display = 1

    help_button_x, help_button_y, help_button_w, help_button_h = help_button

    # Need to check all four limits of button
    if (x > help_button_x and x < help_button_x + help_button_w and
            y > help_button_y and y < help_button_y + help_button_h) and screen_display == 0:
        screen_display = 2

    try_again_button_x, try_again_button_y, try_again_button_w, try_again_button_h = try_again_button

    # Need to check all four limits of button
    if (x > try_again_button_x and x < try_again_button_x + try_again_button_w and
            y > try_again_button_y and y < try_again_button_y + try_again_button_h) and screen_display == 4:
        screen_display = 1


def square_collision(x ,y):
    """

    :param x:
    :param y:
    :return:
    """
    global left_car, right_car, car_y

    a = math.fabs(x - left_car)
    b = math.fabs(y - car_y)
    c = math.sqrt(a**2 + b**2)

    if c <= ((car_width + rect_width)/2):
        return True

    a2 = math.fabs(x - right_car)
    b2 = math.fabs(y - car_y)
    c2 = math.sqrt(a2**2 + b2**2)

    if c2 <= ((car_width + rect_width)/2):
        return True


def circle_collision(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    a = math.fabs(x - left_car)
    b = math.fabs(y - car_y)
    c = math.sqrt(a**2 + b**2)

    if c <= ((car_width + rect_width)/2):
        return True

    a2 = math.fabs(x - right_car)
    b2 = math.fabs(y - car_y)
    c2 = math.sqrt(a2**2 + b2**2)

    if c2 <= ((car_width + rect_width)/2):
        return True


def main_menu():
    """

    :return:
    """
    background = arcade.load_texture("images/menu_background.gif")
    arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, background)

    start = arcade.load_texture("images/start_button.png")
    arcade.draw_xywh_rectangle_textured(start_button[0],
                                        start_button[1],
                                        start_button[2],
                                        start_button[3],
                                        start)

    instruction = arcade.load_texture("images/help_button.png")
    arcade.draw_xywh_rectangle_textured(help_button[0],
                                        help_button[1],
                                        help_button[2],
                                        help_button[3],
                                        instruction)


def instruction_screen():
     pass


def game_screen():
    """

    :return:
    """
    # draw outline of game
    for i in range(WIDTH):
        if i % 100 == 0:
            arcade.draw_line(i, 0, i, HEIGHT, arcade.color.BLACK, 5)
        if i == 200:
            arcade.draw_line(i, 0, i, HEIGHT, arcade.color.BLACK, 10)

    # draws the two chars
    arcade.draw_rectangle_outline(left_car,
                                  car_y,
                                  car_width,
                                  car_width,
                                  arcade.color.BLUE,
                                  5,
                                  left_car_tilt)

    arcade.draw_rectangle_outline(right_car,
                                  car_y,
                                  car_width,
                                  car_width,
                                  arcade.color.RED, 5, right_car_tilt)

    for x, y in zip(x_circle, y_circle):
        arcade.draw_circle_filled(x, y,
                                  ball_radius,
                                  arcade.color.BLUE)

    for f, t in zip(x_square, y_square):
        arcade.draw_rectangle_filled(f, t,
                                     rect_width,
                                     rect_width,
                                     arcade.color.RED)


def game_over_screen():
    """

    :return:
    """
    game_over = arcade.load_texture("images/game_over_screen_.jpg")
    arcade.draw_texture_rectangle(WIDTH//2,
                                  HEIGHT//2,
                                  WIDTH,
                                  HEIGHT,
                                  game_over)

    try_again = arcade.load_texture("images/try_again.png")
    arcade.draw_xywh_rectangle_textured(try_again_button[0],
                                        try_again_button[1],
                                        try_again_button[2],
                                        try_again_button[3],
                                        try_again)

    main_menu_speech = arcade.load_texture("images/main_menu_speech.png")
    arcade.draw_xywh_rectangle_textured(200,
                                        80,
                                        200,
                                        100,
                                        main_menu_speech)


def on_update(delta_time):
    """

    :param delta_time:
    :return:
    """
    global left_car, left_acceleration, left_velocity,left_car_tilt, right_acceleration, right_acceleration,\
        right_velocity, right_car, right_car_tilt, screen_display, score

    if screen_display == 1:
        # constantly updates velocity and acceleration for both cars
        left_velocity += left_acceleration
        left_car += left_velocity

        right_velocity += right_acceleration
        right_car += right_velocity

        # dictates how far the car can move before stopping
        if left_car >= 150:
            left_velocity = 0
            left_acceleration = 0
            left_car_tilt = 0
            left_car = 150
        elif left_car <= 50:
            left_velocity = 0
            left_acceleration = 0
            left_car_tilt = 0
            left_car = 50

        if right_car >= 350:
            right_velocity = 0
            right_acceleration = 0
            right_car_tilt = 0
            right_car = 350
        elif right_car <= 250:
            right_velocity = 0
            right_acceleration = 0
            right_car_tilt = 0
            right_car = 250

        for index in range(len(y_circle)):
            y_circle[index] -= 4
            y_square[index] -= 4

            # if circle reaches bottom of screen, show game over screen
            if y_circle[index] < 0:
                screen_display = 4

            # if square reaches bottom of screen, re draw with random x and y values
            if y_square[index] < 0:
                y_square[index] = random.randrange(HEIGHT, HEIGHT+50)
                x_square[index] = x_pos[random.randrange(len(x_pos))]

            if square_collision(x_square[index], y_square[index]) is True:
                screen_display = 4

            if circle_collision(x_circle[index], y_circle[index]) is True:
                y_circle[index] = random.randrange(HEIGHT, HEIGHT+50)
                x_circle[index] = x_pos[random.randrange(len(x_pos))]
                score += 1
    #print(screen_display)


def on_draw():
    """

    :return:
    """
    arcade.start_render()
    if screen_display == 0:
        main_menu()
    elif screen_display == 1:
        game_screen()
    elif screen_display == 2:
        pass
    elif screen_display == 3:
        pass
    elif screen_display == 4:
        game_over_screen()


def setup():
    """
    
    :return:
    """
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
