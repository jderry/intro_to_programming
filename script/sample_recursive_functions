def recursFunc(n):
    if n > 0:
        return recursFunc(n-1)
    else:
        return n

def recursFactorial(n):
    z = 1
    if n > 1:
        z = n * recursFactorial(n-1)
    return z

def recursEuclidGCD(u, v):
    if u % v:
        return recursEuclidGCD(v, u % v)
    else:
        return v

def recursFib(i):
    if i < 2:
        return i
    else:
        return recursFib(i-1) + recursFib(i-2)

# memoized recursive fibonacci
memoTable = {} # dictionary of index/value pairs
def memoizedFib(i):
    if i <= 2:
        return 1
    if i in memoTable:
        return memoTable[i]
    memoTable[i] = memoizedFib(i-1) + memoizedFib(i-2)
    return memoTable[i]