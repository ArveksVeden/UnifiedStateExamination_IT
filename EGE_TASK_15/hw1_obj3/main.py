def f(A, x, y):
    return ((x <= 3) <= (x**2 <= A)) and ((y**2 <= A) <= (y <= 3))


data = []
for A in range(1, 1000):
    if all(f(A, x, y) for x in range(1, 100) for y in range(1, 100)):
        data.append(A)
print(max(data))