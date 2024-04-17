def f(A, x):
    return ((x % 20 == 0) <= (x % 11 != 0)) or (x + A >= 300)


for A in range(1, 1000000):
    if all(f(A, x) for x in range(1, 10000)):
        print(A)
        break
