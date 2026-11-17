import math

x1 = 1e-8
c1 = abs(x1 * (1 / (2 * math.sqrt(x1))) / math.sqrt(x1))
print("1:", c1)

x2 = 1.001
c2 = abs(x2 * (1 / x2) / math.log(x2))
print("2:", c2)

x3 = 1.000001
c3 = abs(x3 * 1 / (x3 - 1))
print("3:", c3)

x4 = math.pi / 2
c4 = abs(x4 * math.cos(x4) / math.sin(x4))
print("4:", c4)
