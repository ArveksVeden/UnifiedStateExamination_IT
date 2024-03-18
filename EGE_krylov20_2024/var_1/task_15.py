def f(A, x, y):
    return (4 * x + y < A) or (x < y) or (22 <= x)


for A in range(1, 100000):
    if all(f(A, x, y) for x in range(1, 200) for y in range(1, 200)):
        print(A)
        break
