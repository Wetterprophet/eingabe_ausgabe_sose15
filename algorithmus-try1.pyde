#size(1188,420)

#if iniy1 == iniy2 :
#    iniy2 = int(random(0,height))




def setup():
    size(1188,420)
    inix = int(random(0,10))
    iniy1 = int(random(0,height))
    iniy2 = int(random(0,height))
    background(255)
    stroke(0)

#    initialstrokewidth = int(random (3,10)
#    strokeWeight(initialstrokewidth)
    line(inix, iniy1, inix, iniy2)
    print(iniy1, iniy2)



def draw():
    inix = int(random(0,10))
    iniy1 = int(random(0,height))
    iniy2 = int(random(0,height))
    y1= int(random(0,height))
    noFill()
    beginShape()
    vertex(inix, iniy1)
    vertex(int(random(inix,width)),y1)
    vertex(inix,iniy2)
    endShape()
