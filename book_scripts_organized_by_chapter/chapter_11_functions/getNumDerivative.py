def getNumDerivative(f, x, h=1e-11):
    return (f(x + h) - f(x)) / h
