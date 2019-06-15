import arcade

arcade.open_window(400, 400, "My Arcade Game")
arcade.set_background_color(arcade.color.WHITE)
arcade.draw_rectangle_filled(300, 300, 100, 100, arcade.color.BLACK)
arcade.draw_circle_filled(200, 200, 1, arcade.color.WHITE)
arcade.run()

