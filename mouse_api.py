############################ (c) TEAM SIMULATORS #######################
#   
#        @ black_perl
#
#######################################################################

import Xlib 
from Xlib import X , display
import time
# Xlib library for interfacing the WindowX server and python 

d = display.Display() #getting the display object representing the screen of window X server
s = d.screen()
root = s.root

# defining some global_variables

LEFT = 1
RIGHT = 3
DOUBLE = 2
SCROLL_UP = 4
SCROLL_DOWN = 5

class Mouse():
    ''' abstract representaion of the virtual mouse'''
    def mouseMove(self, x, y):
        '''function for moving the mouse
        to a new position x , y '''
        self.X = x
        self.Y = y
        root.warp_pointer(x,y) # moving the pointer to x,y coordinate on screen
        d.sync() # making the event actually happen
     
        

    def mouseEvent(self, event, 
                   delay=0.01,
                   async = False):
        ''' function for representing different different clicks'''
        Xlib.ext.xtest.fake_input(d, X.ButtonPress, event)
        d.sync()
        time.sleep(delay) # setting a delay time for the click
        if not async:
            Xlib.ext.xtest.fake_input(d, X.ButtonRelease, event); 
            d.sync()
    

    def sync(self): 
        '''for doing syncing of unsynced events'''
        d.sync()
    
  


