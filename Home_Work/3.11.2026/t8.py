import math
import mpmath

mpmath.mp.dps = 50

for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    bad = math.log(1.0 + x)
    good = math.log1p(x)
    
    xm = mpmath.mpf(str(x))
    exact = mpmath.log(1 + xm)
    
    err_bad = abs(mpmath.mpf(bad) - exact) / abs(exact)
    err_good = abs(mpmath.mpf(good) - exact) / abs(exact)
    
    print("x =", x)
    print("err_bad =", float(err_bad))
    print("err_good =", float(err_good))
