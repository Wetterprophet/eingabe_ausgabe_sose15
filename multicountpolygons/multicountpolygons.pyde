hght = 420
wdth = 1188
#size(1188,420)               #define window size - doesnt work unless in setup
inix = int(random(10,50))                    #define x as first value for loop
iniy1 = int(random(0,hght))    #define y1 as random between 0 and 420=height, no global value yet
#iniy2 = iniy1
iniy2 = int(random(0,hght))    #define y2 ---"--- , start values for first line
while iniy1 == iniy2 :           
    iniy2 = int(random(0,hght))    #iniy1 and iniy2 shouldnt be the same value
cnt = 0                     #define count and assign value 0
x = 0
isw = int(random (1,5))    #initial strokeweight random


x_values=[]                 #create a list to hold the x values
y_values=[]                 #create a list to hold the y values

cnt = -1                    #define count and assign value -1 -> first loop cnt#0
sides = 2                   #define sides and assign value 2 -> first polygon has 3 sides
nr_of_xy_values = 1         #
delta_xy = 1
edges=sides

edgesdone=0






def setup():
    global x
    background(255)           #white bg (RGB)
    stroke(0)                 #black stroke
    size(wdth,hght)            #define window size 
    x= inix    

    strokeWeight(isw)
    line(inix, iniy1, inix, iniy2)   #draws the initial vertical line
    x_values.append(inix)
    x_values.append(inix)
    y_values.append(iniy1)
    y_values.append(iniy2)

    print("X",x_values,"Y", y_values)





#while cnt =< hour():    




def draw():
    cnt = cnt+1                 #variable cnt goes up by value 1 -> first loop == cnt0
    sides = sides+1             #variable sides goes up by value 1 -> first polygon 3 sides...
    delta_xy = delta_xy+1       #variable delta_xy goes up by value 1 -> 1 point more each loop
    nr_of_xy_values = nr_of_xy_values + delta_xy     #make sure there are enough values to store points for all our polygons
    
    first_xy_value = int random(nr_of_xy_values-sides+1;nr_of_xy_values-count-1)     #use open points of the old polygon to set first point of new polygon
    second_xy_value = first_xy_value + 1                                             #set next point of old polygon as second start point for new polygon
    
    
    
    
    
    
    
    
    
    delay(100)
    global x, inix, cnt, isw
 
    
      
        
    y=year()
    mo=month()
    d=day() 
    h=hour()
    m=minute()
    s=second()
    timestamp = str(str(y)+"-"+str(mo)+"-"+str(d)+"-"+str(h)+"-"+str(m)+"-"+str(s))
 #   print(timestamp)

    
 
    
#    while cnt<= second():
        
#    noLoop()
        
    cnt=cnt+1
    print ('count',  cnt)
        
        
        
    colorMode(HSB, 255)       #set color mode to HSB - max value = 255
    hu= int(random(0,255))    #random color
    sa= int(random(150,255))
    br= int(random(150,255))
    op= int(random(50,200))
    stroke(hu,255,50,)
        
    y1= int(random(0,height))
    x1= int(random(inix, width))
    x_values.append(x1)
    y_values.append(y1)
    print("X",x_values,"Y", y_values)
    fill(hu,sa,br,op)
    strokeWeight(isw)           #define width of stroke
    beginShape()
    vertex(x_values[-3], y_values[-3])
    vertex(x_values[-2], y_values[-2])
    vertex(x_values[-1], y_values[-1])
    vertex(x_values[-3], y_values[-3])
    endShape()
    saveFrame("my-image-" + timestamp +".png")
    

#    beginShape()
#    while    
#            
#                    
    
    
    
    
    
    
def mousePressed():
    loop()                 #Holding down the mouse activates looping

def mouseReleased():
    noLoop()                   #Releasing the mouse stops looping draw()
