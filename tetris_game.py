import arcade

# Set how many rows and columns we will have
ROW_COUNT = 18
COLUMN_COUNT = 22

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid = []

block_x = 15
block_y = 365

gravity = 25
time = 0

right_pressed = False
left_pressed = False
down_pressed = False

def on_update(delta_time):
    global right_pressed, left_pressed, down_pressed, block_x, block_y, time

    time += 1

    if time == 10:
        block_y -= 25
        time = 0

    if right_pressed and block_x <= 265:
        block_x += 25

    if left_pressed and block_x >= 40:
        block_x -= 25

    if down_pressed and block_y >= 40:
        block_y -= 25

    if block_x > 360:
        if right_pressed:
            block_x += 0

    print(delta_time)
def on_draw():
    global block_x, block_y

    arcade.start_render()
    # Draw the grid
    for row in range(18):
        for column in range(12):
            # Figure out what color to draw the box

            # Do the math to figure out where the box is
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

            # Draw the box
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, arcade.color.WHITE)

    arcade.draw_rectangle_filled(430, 235, 250, 500, arcade.color.BEIGE)

    arcade.draw_rectangle_filled(block_x, block_y, 20, 20, arcade.color.PURPLE_PIZZAZZ)

def on_key_press(key, modifiers):
    global right_pressed, left_pressed, down_pressed, block_x, block_y

    if key == arcade.key.D:
        right_pressed = True

    if key == arcade.key.A:
        left_pressed = True

    if key == arcade.key.S:
        down_pressed = True

def on_key_release(key, modifiers):
    global right_pressed, left_pressed, down_pressed, block_x, block_y

    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.S:
        down_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    global grid

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(on_update, 1 / 10)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    # array is simply a list of lists.
    for row in range(ROW_COUNT):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COLUMN_COUNT):
            grid[row].append(0)  # Append a cell

    arcade.run()


if __name__ == '__main__':
    setup()
