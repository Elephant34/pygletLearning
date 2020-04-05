import pyglet

window = pyglet.window.Window(500, 400, caption="Hello World")

label = pyglet.text.Label(
    "Hello World",
    font_name="Arial",
    font_size=25,
    x=window.width//2,
    y=window.height//2,
    anchor_x="center",
    anchor_y="center"
)

'''
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)
'''

@window.event
def on_draw():
    window.clear()
    label.draw()

'''
@window.event
def on_key_press(symbol, modifiers):
    print("Key pressed: {} {}".format(symbol, modifiers))

@window.event
def on_mouse_press(x, y, button, modifiers):
    print("Mouse button : {} {} pressed at {} {}".format(button, modifiers, x, y))
'''

pyglet.app.run()