import pgzrun
from random import randint 
# by inputing the randint function, i can make the colours that appear on the screen to be different


#forgot how to run the project, all i could remember was the command prompt in the files location
WIDTH = 300

HEIGHT = 300
'```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````'
def draw():
    width = WIDTH
    height = HEIGHT-200

    r = 255
    g = 0
    b = randint(100,255)
  
# Want help on how I can make the pattern different and help on how to make the circle class function

# Sorry if it looks the same, had trouble understanding some things.

    for drawing in range(30):
        drawings = Rect((0,0), (width, height))
        #drawings.center = (150, 150)
        screen.draw.rect(drawings, (r,g,b))


        width -= 10
        height += 10
        r -= 20
        g += 20

pgzrun.go()

