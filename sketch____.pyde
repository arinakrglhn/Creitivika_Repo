def setup():
    size(1000,1000)
    background(0)
def draw():
    global Left
   
 
   
    if mouseButton ==LEFT:
        fill(13,150,222)
        ellipse(600,400,90,300)#ухо
        ellipse(400,400,90,300) #ухо
        ellipseMode(CENTER)
        ellipse(500,500,250,250) #голова
        fill(0)
        ellipse(500,500,10,10)#nose
        fill(102,105,113)
        ellipse(450,450,50,50)#глаз
        ellipse(550,450,50,50)#глаз
        fill(227,255,250)
        ellipse(500,550,50,30)
    else:
        background(0)
