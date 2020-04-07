'''
Testing with how classes intergrate with pyglet
'''
import pyglet

class Screen(pyglet.window.Window):
    '''
    A main screen class
    '''

    def __init__(self, width, height):
        super().__init__(width, height)
    
    def on_draw(self):
        '''
        Hopfully overrides the default draw function
        '''
        self.clear()

        test_lbl.draw()



window = Screen(800, 600)
window.set_caption("Window experiment")

test_lbl = pyglet.text.Label(text="test", x=window.width//2, y=window.height//2, color=(255,0,255,255))

if __name__ == "__main__":
    pyglet.app.run()