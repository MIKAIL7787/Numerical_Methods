import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=1_000_000)

t_loop = float("inf")
r_loop = None
for _ in range(3):
    t0 = time.perf_counter()
    max_val = a[0]
    max_idx = 0
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop:
        t_loop = t1 - t0
        r_loop = (max_val, max_idx)

t_np = float("inf")
r_np = None
for _ in range(3):
    t0 = time.perf_counter()
    m_val = a.max()
    m_idx = a.argmax()
    t1 = time.perf_counter()
    if (t1 - t0) < t_np:
        t_np = t1 - t0
        r_np = (m_val, m_idx)

print("цикл:", t_loop*1000, "мс")
print("NumPy:", t_np*1000, "мс")
print("ускорение:", t_loop / t_np)
print("результаты совпадают:", r_loop[0] == r_np[0] and r_loop[1] == r_np[1])
