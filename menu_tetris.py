import arcade


WIDTH = 305
HEIGHT = 460

grid_height = 20
grid_width = 20
MARGIN = 5

column_count = 12
row_count = 18

grid = []
grid_cords = []

def on_draw():
    arcade.start_render()

    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == 0:
                colour = arcade.color.WHITE


            x = (MARGIN + grid_width) * column + MARGIN + grid_width // 2
            y = (MARGIN + grid_height) * row + MARGIN + grid_height // 2


            arcade.draw_rectangle_outline(x, y, grid_width, grid_height, colour)




def on_update(delta_time):
    pass


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    row = y // (grid_height + MARGIN)
    column = x // (grid_width + MARGIN)

    print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")


def setup():

    for row in range(row_count):
        grid.append([])
        for column in range(column_count):
            grid[row].append(0)



    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    print(grid_cords)

    arcade.run()


if __name__ == '__main__':
    setup()
