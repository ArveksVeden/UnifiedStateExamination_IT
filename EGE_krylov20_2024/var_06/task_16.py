def f(n):
    if n < 3: return n
    if n > 2 and n % 2 == 0: return 3 * (n - 1) + f(n - 1) + 5
    if n > 2 and n % 2 != 0: return 3 * (n - 1) + f(n - 2) - 2


print(f(35))
