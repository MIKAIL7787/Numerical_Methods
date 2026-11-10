import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    out = a.copy()
    for i in range(len(out)):
        if out[i] < 0:
            out[i] = 0.0
        elif out[i] > 1:
            out[i] = 1.0
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = out

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    out_np = np.clip(a, 0, 1)
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = out_np

changed = np.sum((a < 0) | (a > 1))

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("результаты совпадают:", np.allclose(r_loop, r_np))
print("изменено элементов:", changed)
