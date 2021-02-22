# A function to calculate the distance between rider and driver 
import math

def distance(x1,y1,x2,y2):

    #formula to calculate distance
    c1 = (x2 - x1)
    c2 = (y2 - y1)
    return (math.sqrt((c1**2)+(c2**2)))