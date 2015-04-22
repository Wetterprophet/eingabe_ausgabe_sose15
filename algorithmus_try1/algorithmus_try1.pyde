# initialize the variables global
inix = 0
iniy1 = 0
iniy2 = 0

def setup():
    size(1188, 420)
    # now assign new values based on the 
    # width and height of your sketch
    inix = int(random(0, 10))
    iniy1 = int(random(0, height))
    iniy2 = int(random(0, height))
    while iniy1 == iniy2:
        iniy2 = int(random(0, height))
    print inix, iniy1, iniy2
    background(255)
    stroke(0)
#    initialstrokewidth = int(random (3,10)
#    strokeWeight(initialstrokewidth)
    #line(inix, iniy1, inix, iniy2)
    #print(iniy1, iniy2)


def draw():
    y1 = int(random(0, height))
    noFill()
    beginShape()
    vertex(inix, iniy1)
    vertex(int(random(inix, width)), y1)
    vertex(inix, iniy2)
    endShape()

