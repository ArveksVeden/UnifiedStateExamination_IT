def f(A, x, y):
    return (3*x + y > A) and (y < x) and (x < 30)


for A in range(100000):
    if all(not f(A, x, y) for x in range(1000) for y in range(1000)):
        print(A)
        break