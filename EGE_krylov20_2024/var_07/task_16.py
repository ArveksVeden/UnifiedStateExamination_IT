def f(n):
    if n < 3: return 1
    if n > 2 and n % 2 != 0: return f(n - 1) + f(n - 2)
    if n > 2 and n % 2 == 0: return sum([f(p) for p in range(1, n)])


print(f(24))
