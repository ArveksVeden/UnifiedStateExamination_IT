def f(n):
    if n == 1: return 1
    if n == 2: return 1
    if n > 2 and n % 2 == 0: return 2 + f(n - 1)
    if n > 2 and n % 2 != 0: return 3 * n + f(n - 2)


print(f(43))