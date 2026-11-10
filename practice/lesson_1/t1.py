import time
import numpy as np

rng = np.random.default_rng(42)

a_5 = rng.normal(size=100_000)
t_loop_5 = float("inf")
r_loop_5 = None
for _ in range(3):
    t0 = time.perf_counter()
    total = 0.0
    for x in a_5:
        total += x
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop_5:
        t_loop_5 = t1 - t0
        r_loop_5 = total

t_np_5 = float("inf")
r_np_5 = None
for _ in range(3):
    t0 = time.perf_counter()
    res = a_5.sum()
    t1 = time.perf_counter()
    if (t1 - t0) < t_np_5:
        t_np_5 = t1 - t0
        r_np_5 = res

a_6 = rng.normal(size=1_000_000)
t_loop_6 = float("inf")
r_loop_6 = None
for _ in range(3):
    t0 = time.perf_counter()
    total = 0.0
    for x in a_6:
        total += x
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop_6:
        t_loop_6 = t1 - t0
        r_loop_6 = total

t_np_6 = float("inf")
r_np_6 = None
for _ in range(3):
    t0 = time.perf_counter()
    res = a_6.sum()
    t1 = time.perf_counter()
    if (t1 - t0) < t_np_6:
        t_np_6 = t1 - t0
        r_np_6 = res

a_7 = rng.normal(size=10_000_000)
t_loop_7 = float("inf")
r_loop_7 = None
for _ in range(3):
    t0 = time.perf_counter()
    total = 0.0
    for x in a_7:
        total += x
    t1 = time.perf_counter()
    if (t1 - t0) < t_loop_7:
        t_loop_7 = t1 - t0
        r_loop_7 = total

t_np_7 = float("inf")
r_np_7 = None
for _ in range(3):
    t0 = time.perf_counter()
    res = a_7.sum()
    t1 = time.perf_counter()
    if (t1 - t0) < t_np_7:
        t_np_7 = t1 - t0
        r_np_7 = res

print("n = 10^5 | цикл:", t_loop_5*1000, "мс | NumPy:", t_np_5*1000, "мс | ускорение:", t_loop_5 / t_np_5)
print("n = 10^6 | цикл:", t_loop_6*1000, "мс | NumPy:", t_np_6*1000, "мс | ускорение:", t_loop_6 / t_np_6)
print("n = 10^7 | цикл:", t_loop_7*1000, "мс | NumPy:", t_np_7*1000, "мс | ускорение:", t_loop_7 / t_np_7)
