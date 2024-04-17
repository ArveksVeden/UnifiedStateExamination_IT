def f(A, x, y):
    return (x >= 20) or (y >= 40) or (y <= x + A) or (y >= 3*x - A)


for A in range(10000):
    if all(f(A, x, y) for x in range(200) for y in range(200)):
        print(A)
        break
