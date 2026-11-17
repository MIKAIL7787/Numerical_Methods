import math

xs = [1e-4, 1e-8, 1e-12, 1e-15, 1e-16]

for x in xs:
    bad = (math.exp(x) - 1) / x
    good = 1 + x / 2 + (x * x) / 6
    print("x =", x, "bad =", bad, "good =", good)
