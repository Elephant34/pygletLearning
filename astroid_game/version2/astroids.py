'''
Atroids game following pyglet tutorial
Best way to learn is to make
'''
import pyglet
from game import resources, load, player

game_window = pyglet.window.Window(800, 600)
game_window.set_caption("My Amazing Game")

@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)

main_batch = pyglet.graphics.Batch()

score_lbl = pyglet.text.Label(
    text="Score: 0",
    x=10,
    y=game_window.height - 20,
    batch=main_batch
)
level_lbl = pyglet.text.Label(
    text="My Amazing Game",
    x=game_window.width//2,
    y=game_window.height//2,
    anchor_x="center",
    batch=main_batch
)

player = player.Player(x=400, y=300, batch=main_batch)
game_window.push_handlers(player)

asteroids = load.astroids(5, player.position, batch=main_batch)
lives = load.player_lives(3, batch=main_batch)

game_objects = [player] + asteroids

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()