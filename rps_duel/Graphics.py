"""
draw a graphical interface using python arcade
"""
import arcade
import os

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Rps Duel"
# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.7
CHARACTER2_SCALING = 0.4
TILE_SCALING = 0.1


class GameWindow(arcade.Window):
    """
    draw game screen window
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.player1_list = None
        self.player2_list = None
        # Separate variable that holds the player sprite
        self.player1_sprite = None
        self.player2_sprite = None
        self.background = None

    def setup(self):
        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()
        self.background = arcade.load_texture(os.path.join("images", "background.jpg"))

        image_source_p1 = os.path.join("images", "wizard.png")
        self.player1_sprite = arcade.Sprite(image_source_p1, CHARACTER_SCALING)
        self.player1_sprite.center_x = 160
        self.player1_sprite.center_y = 280
        self.player1_list.append(self.player1_sprite)

        image_source_p2 = os.path.join("images", "yennefer.png")
        self.player2_sprite = arcade.Sprite(image_source_p2, CHARACTER2_SCALING)
        self.player2_sprite.center_x = 1060
        self.player2_sprite.center_y = 260
        self.player2_list.append(self.player2_sprite)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )
        self.player1_list.draw()
        self.player2_list.draw()



def main():
    window = GameWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
