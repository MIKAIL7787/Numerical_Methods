import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    res = [x for x in a if x > 0]
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = res

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    res_np = a[a > 0]
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = res_np

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("результаты совпадают:", np.allclose(r_loop, r_np))
