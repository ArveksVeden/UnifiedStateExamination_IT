def f(A, x, y):
    return (84 != 2*x + y) or (A < x) or (A < y)


data = []
for A in range(1, 1000):
    if all(f(A, x, y) for x in range(1, 100)\
           for y in range(1, 100)):
        data.append(A)
print(max(data))