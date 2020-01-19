""" servo pyfirmata"""

import pyfirmata
from tkinter import *

def move_servo(angle):
    pin9.write(angle)
    
def main():
    global pin9
    
    board=pyfirmata.Arduino('COM5')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    
    root = Tk()
    scale = Scale(root, command = move_servo, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Angle')
    scale.pack(anchor = CENTER)

    root.mainloop()

main()
