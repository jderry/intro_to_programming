def numBalls(dollars: float, inches: float) -> int:
    ''' Given available dollars desired radius of balls,
        calculate how many red, blue, or green balls
        of that size you can buy.
    '''
    from numBalls_sbr import calculateSurfaceArea, computeCostsByColor, printNumBallsByColor
    
    area = calculateSurfaceArea(inches)
    costDict = computeCostsByColor(area)
    printNumBallsByColor(inches, dollars, costDict)

