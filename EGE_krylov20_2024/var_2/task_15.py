def f(A, x, y):
    return (x**2 + y**2 > 128) or (y < -x + A)


for A in range(1000000):
    if all(f(A, x, y) for x in range(200) for y in range(200)):
        print(A)
        break
