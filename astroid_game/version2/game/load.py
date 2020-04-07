import pyglet
import random
import math
from game import resources, physicalObject

def astroids(num, player_pos, batch=None):
    '''
    Loads astroids in random positions
    '''
    asteroids = []


    
    for i in range(num):
        # Sets the inital positon so they don't all go to same point
        x, y = player_pos
        while distance((x,y), player_pos) < 100:
            x = random.randint(0, 800)
            y = random.randint(0, 600)

        new_astroid = physicalObject.PhysicalObject(
            img=resources.images["asteroid"],
            x=x,
            y=y,
            batch=batch
        )
        new_astroid.rotation = random.randint(0, 360)
        new_astroid.velocity_x = random.random()*40
        new_astroid.velocity_y = random.random()*40

        asteroids.append(new_astroid)
    
    return asteroids

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def player_lives(num_icons, batch=None):
    player_lives = []

    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(
            img=resources.images["player"],
            x=785-i*30,
            y=585,
            batch=batch
        )

        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives