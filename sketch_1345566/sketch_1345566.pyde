x=0
y=0
mode="b" # b - больше, m - меньше
def setup():
    size(1000,1000)
    background(45,181,214)
def draw():
    global x,y,mode
    rectMode(CENTER)
    #rect(400,400,100,100)
    translate(400,400)
    rotate(x)
    
    rect(0,0,x,x)
    
    if mode=="b":
        x=x+10

    if mode=="m":
        x=x-10

    
    print(x)
    print(y)
    if x>=500:
       mode="m"

    if x<=0:
        mode="b"

    
    
