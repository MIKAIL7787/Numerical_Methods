a = 1 + 1e-8
b = 1.0
f = a - b

cond_a = abs(a / (a - b))
delta_a = 1e-9

a_new = a * (1 + delta_a)
f_new = a_new - b

df_rel = abs(f_new - f) / abs(f)
pred = cond_a * delta_a

print("cond_a:", cond_a)
print("Fakt:", df_rel)
print("Teoriya:", pred)
