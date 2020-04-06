'''
Atroids game following pyglet tutorial
Best way to learn is to make
'''
import pyglet
from game import resources, load

game_window = pyglet.window.Window(800, 600)
game_window.set_caption("My Amazing Game")

@game_window.event
def on_draw():
    game_window.clear()

    score_lbl.draw()
    level_lbl.draw()

    player.draw()

    for asteroid in asteroids:
        asteroid.draw()


score_lbl = pyglet.text.Label(
    text="Score: 0",
    x=10,
    y=game_window.height - 20
)
level_lbl = pyglet.text.Label(
    text="My Amazing Game",
    x=game_window.width//2,
    y=game_window.height//2,
    anchor_x="center"
)

player = pyglet.sprite.Sprite(img=resources.images["player"], x=400, y=300)

asteroids = load.astroids(5, player.position)

if __name__ == "__main__":
    pyglet.app.run()