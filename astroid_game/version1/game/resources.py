import pyglet

def center_image(image):
    '''
    Sets an images anchor point to the middle
    This is where it pivots around
    '''
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

images = {
    "player": pyglet.resource.image("player.png"),
    "bullet": pyglet.resource.image("bullet.png"),
    "asteroid": pyglet.resource.image("asteroid.png"),
}
for image in images:
    center_image(images[image])