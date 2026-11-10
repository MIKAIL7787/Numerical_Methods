import time
import math
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    s = 0.0
    sq_s = 0.0
    n = len(a)
    for x in a:
        s += x
        sq_s += x * x
    mean = s / n
    variance = (sq_s / n) - (mean ** 2)
    std = math.sqrt(variance)
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = (mean, std)

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    m_val = a.mean()
    s_val = a.std()
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = (m_val, s_val)

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("совпадают до 1e-12:", np.allclose(r_loop, r_np, atol=1e-12, rtol=1e-12))
