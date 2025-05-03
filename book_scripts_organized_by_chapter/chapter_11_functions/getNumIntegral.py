def getNumIntegral(f, end_x, start_x=0, delta_x=1e-8):
    from numpy import linspace, sum as s
    x = linspace(start_x, end_x, int((end_x - start_x) / delta_x))
    return s(f(x) * delta_x)

