x=100
y=100
def setup():
    size(300,300)
def draw():
    # rect(100,100,100,100)
    global x , y
    rectMode(CENTER)
    rect(150,150,x,y)
    x=x+13
    y=y+13
    print(x)
    if x>=300:
       x=100
       y=100 
