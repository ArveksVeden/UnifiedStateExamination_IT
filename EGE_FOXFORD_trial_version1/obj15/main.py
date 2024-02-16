def f(A, x):
    return ((x % 6 == 0) <= (x % 14 != 0)) or (x + A >= 85)

for A in range(1, 100):
    if all(f(A, x) for x in range(1, 100)):
        print(A)
        break
