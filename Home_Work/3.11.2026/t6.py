import math
import mpmath

mpmath.mp.dps = 50

for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    bad = (1.0 - math.cos(x)) / (x * x)
    good = 2.0 * (math.sin(x / 2.0) ** 2) / (x * x)
    
    xm = mpmath.mpf(str(x))
    exact = (1 - mpmath.cos(xm)) / (xm * xm)
    
    err_bad = abs(mpmath.mpf(bad) - exact) / abs(exact)
    err_good = abs(mpmath.mpf(good) - exact) / abs(exact)
    
    print("x =", x, "log_x =", math.log10(x))
    print("log_err_bad =", math.log10(float(err_bad)))
    print("log_err_good =", math.log10(float(err_good)))
