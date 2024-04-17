def f(n):
    if n < 3: return n
    if n > 2 and n % 2 == 0: return 2 * (n - 1) + f(n - 1) + 2
    if n > 2 and n % 2 != 0: return 2 * (n + 1) + f(n - 2) - 5


print(32)
