def calculateSurfaceArea(inches: float) -> float:
    from math import pi
    return 4 * pi * inches**2

def computeCostsByColor(area: float) -> dict:
    return {'red': area * .03, 'blue': area * .05, 'green': area * .08}

def printNumBallsByColor(inches: float, dollars: float, costDict: dict):
    print(f"\nThe number of {inches:4.2f}-inch balls "
          f"you can buy with ${dollars:4.2f} dollar(s) by color is:")
    for color, cost in costDict.items():
        numBalls = int(dollars / cost)
        print(f"{color:<6} {numBalls}")
