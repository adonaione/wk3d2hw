import math


def area_of_cir(radius):
    radius = int(radius)
    area = (radius * 3.141592) ** 2
    print(area)

def hypotenuse(side, side2):
    side = int(side)
    side2= int(side2)
    hyp = math.sqrt((side**2) + (side2**2))
    print(hyp)