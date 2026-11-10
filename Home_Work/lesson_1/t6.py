import time
import numpy as np

rng = np.random.default_rng(42)
m = rng.normal(size=(100_000, 10))

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    rows = m.shape[0]
    cols = m.shape[1]
    out = m.copy()
    means = [0.0] * cols
    for j in range(cols):
        s = 0.0
        for i in range(rows):
            s += m[i, j]
        means[j] = s / rows
    for i in range(rows):
        for j in range(cols):
            out[i, j] -= means[j]
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = out

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    out_np = m - m.mean(axis=0)
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = out_np

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("результаты совпадают:", np.allclose(r_loop, r_np))
