import pyglet
import random
import math
from game import resources

def astroids(num, player_pos):
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

        new_astroid = pyglet.sprite.Sprite(
            img=resources.images["asteroid"],
            x=x,
            y=y
        )
        new_astroid.rotation = random.randint(0, 360)

        asteroids.append(new_astroid)
    
    return asteroids

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)