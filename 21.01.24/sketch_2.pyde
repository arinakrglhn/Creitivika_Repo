x=0
y=0
def setup():
    size(300,300)
def draw():
    ellipse(0,0,0,0)
    global x , y
    ellipseMode(CENTER)
    ellipse(0,0,x,y)
    x=x+10
    y=y+10
    print(x)
    if x==400:
        x=0
        y=0
