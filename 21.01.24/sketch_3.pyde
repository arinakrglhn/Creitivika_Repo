color=0
def setup():
    size(300,300)
def draw():
    ellipse(100,100,100,100)
    global color
    fill(color)
    color=color+1
   
    if color==255:
        color=0
