x=0
mode="вверх"
def setup():
    size(1000,1000)

def draw():
    global x,mode
    background(229,65,65)
    #ellipse(100,500,50,50)
    ellipse(500,x,50,50)
    if mode=="вверх":
      x=x+10
    print (x)
    if x >1000:
        mode="вниз"
    if mode=="вниз":
      x=x-10
    if x <0 :
      mode="вверх"
    
