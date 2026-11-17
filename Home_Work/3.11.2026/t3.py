import math

epsilons = [1e-2, 1e-4, 1e-6]
prev_shift = 0

for eps in epsilons:
    c = 1 - eps
    d = 4 - 4 * c
    x1 = (2 + math.sqrt(d)) / 2
    shift = abs(x1 - 1)
    if prev_shift == 0:
        ratio = "-"
    else:
        ratio = prev_shift / shift
    print(eps, shift, ratio)
    prev_shift = shift
