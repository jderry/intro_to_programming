import pint
ur = pint.UnitRegistry()
Q_ = ur.Quantity

P = (745 * ur.torr).to('atm')
V = (7240 * ur.cu_ft).to('liter')
T = Q_(21, ur.degC).to('degK')

R = 0.0821 * ur.liter * ur.atm / (ur.mol * ur.degK)

n = P * V / (R * T)
n

g_He = n * (4 * ur.g / ur.mol)
g_He

sigFigs, numDigInt = 3, 5
round(g_He, (sigFigs - numDigInt))

g_He.magnitude

g_He.units

print(g_He.dimensionality)

