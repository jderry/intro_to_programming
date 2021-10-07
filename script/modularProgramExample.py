
def convertDimToFeet(inches):
    return inches/12
def computeSurfaceArea(height, radius):
    return 3.14*radius*(radius**2 + height**2)**(1/2)
def computeCostsByColor(area):
    return {'red': area*.10, 'blue': area*.15, 'green': area*.18}
def printResults(area, costDict):
    print(f"\nThe surface area of the cone is: {area:4.2f} square ft.")
    print("\nPainting it:")
    for color, cost in costDict.items():
        print(f"{color:<6}" + " will cost" + f" ${cost:>5.2f}.")
    
    
def conePaint(coneHeight, coneDiameter):
    radius = convertDimToFeet(coneDiameter/2)
    height = convertDimToFeet(coneHeight)
    area = computeSurfaceArea(height, radius)
    costDict = computeCostsByColor(area)
    printResults(area, costDict)
        
        
conePaint(120, 60)



