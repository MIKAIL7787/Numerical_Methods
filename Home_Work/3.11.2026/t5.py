import math
import mpmath

mpmath.mp.dps = 50

a = 1.0
c = 1.0

for b in [1e4, 1e8, 1e12]:
    bad = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    good = (2 * c) / (-b - math.sqrt(b * b - 4 * a * c))
    
    bm = mpmath.mpf(b)
    exact = mpmath.mpf(2) / (-bm - mpmath.sqrt(bm * bm - 4))
    
    err_bad = abs(mpmath.mpf(bad) - exact) / abs(exact)
    err_good = abs(mpmath.mpf(good) - exact) / abs(exact)
    
    print("b =", b)
    print("err_bad =", float(err_bad))
    print("err_good =", float(err_good))
