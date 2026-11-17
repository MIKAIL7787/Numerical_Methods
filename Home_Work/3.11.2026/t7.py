import math
import mpmath

mpmath.mp.dps = 50

for x in [1e4, 1e8, 1e12, 1e14, 1e16]:
    bad = math.sqrt(x + 1.0) - math.sqrt(x)
    good = 1.0 / (math.sqrt(x + 1.0) + math.sqrt(x))
    
    xm = mpmath.mpf(x)
    exact = 1 / (mpmath.sqrt(xm + 1) + mpmath.sqrt(xm))
    
    err_bad = abs(mpmath.mpf(bad) - exact) / abs(exact)
    err_good = abs(mpmath.mpf(good) - exact) / abs(exact)
    
    print("x =", x)
    print("err_bad =", float(err_bad))
    print("err_good =", float(err_good))
