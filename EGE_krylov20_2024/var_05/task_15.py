def f(A, x):
    return ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500)


for A in range(1, 100000):
    if all(f(A, x) for x in range(1, 1000)):
        print(A)
        break
