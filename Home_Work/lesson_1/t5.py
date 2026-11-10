import time
import numpy as np

rng = np.random.default_rng(42)
m = rng.normal(size=(100_000, 10))

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    result = [0.0] * m.shape[0]
    for i in range(m.shape[0]):
        s = 0.0
        for j in range(m.shape[1]):
            s += m[i, j]
        result[i] = s
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = result

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    result_np = m.sum(axis=1)
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = result_np

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("результаты совпадают:", np.allclose(r_loop, r_np))
