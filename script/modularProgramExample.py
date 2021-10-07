# coding: utf-8
def convertDimToFeet(inches):
    return inches/12
def computeSurfaceArea(height, radius):
    return 3.14*radius*(radius**2 + height**2)**(1/2)
def computeCostsByColor(area):
    return {'red': area*.10, 'blue': area*.15, 'green': area*.18}
    
def conePaint(coneHeight, coneDiameter):
    radius = coneDiameter/2
    radius = convertDimToFeet(radius)
    height = convertDimToFeet(coneHeight)
    area = computeSurfaceArea(height, radius)
    costDict = computeCostsByColor(area)
    print("The surface area of the cone is: " + str(area) + " square ft.")
    for color, cost in costDict.items():
        print(f"Painting it in {color} will cost: {cost}.")
        

def conePaint(coneHeight, coneDiameter):
    radius = convertDimToFeet(coneDiameter/2)
    height = convertDimToFeet(coneHeight)
    area = computeSurfaceArea(height, radius)
    costDict = computeCostsByColor(area)
    print(f"\nThe surface area of the cone is: {area:4.2f} square ft.")
    print("\nPainting it:")
    for color, cost in costDict.items():
        print(f"{color:<6}" + " will cost" + f" ${cost:>5.2f}.")
        
        
conePaint(120, 60)
