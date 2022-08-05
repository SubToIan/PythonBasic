from tkinter import *

win = Tk()



map = [['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x'],
       ['x','x','x','x','x','x','x','x','x','x']]


        

class Mario:
    def __init__(self,customization,lives,size,status):
        self.customization=customization
        self.lives=lives
        self.size=size
        self.status=status
        self.x = 4
        self.y = 4

    def right(self):
        self.x = self.x+1

    def left(self):
        self.x=self.x-1

    def down(self):
        self.y=self.y+1

    def up(self):
        self.y=self.y-1

def print_map1():
    # for i in range(10):
    #     row = map[i]
    #     for x in row:
    #         print(x, end=' ')
    #     print()
    for y in range(10):
        for x in range(10):
            print(map[x][y], end=' ')
        print()

def print_map2(obj_x, obj_y, customization):
    # map[x][y]=customization
    for y in range(10):
        for x in range(10):
            if x==obj_x and y==obj_y:
                print(customization, end=' ')
            else:
                print(map[x][y], end=' ')
        print()

def print_map3(mario1, mario2):
    # map[x][y]=customization
    for y in range(10):
        for x in range(10):
            if x==mario1.x and y==mario1.y:
                print(mario1.customization, end=' ')
            elif x==mario2.x and y==mario2.y:
                print(mario2.customization, end=' ')
            else:
                print(map[x][y], end=' ')
        print()


def key_down(e):
    key = e.keysym
    if key == 'Left':
        mario.left()
    elif key == 'Right':
        mario.right()
    elif key == "Up":
        mario.up()
    elif key== "Down":
        mario.down()

    if key == 'a':
        mario2.left()
    elif key == 'd':
        mario2.right()
    elif key == "w":
        mario2.up()
    elif key== "s":
        mario2.down()

    print_map3(mario, mario2)

win.bind('<KeyPress>', key_down)

print_map2(obj_x=4, obj_y=4,customization="o")

mario=Mario(customization="1",lives=5,size=0,status=0)
mario2=Mario(customization="2",lives=5,size=0,status=0)

print ("Use ←↑↓→ to move.")

win.mainloop()



