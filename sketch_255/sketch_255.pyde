x=1
y=1
def setup():
    size(1000,1000)
    background(0)
def draw():
    global x,y
    
    strokeWeight(random(10))
    point(random(1000),random(1000))
   
    x=x+1
    y=y+1
    stroke(64,225,255)
    if mousePressed:
      background(0)
