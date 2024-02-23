def f(A, x, y):
    return (y + 2*x < A) or (y + x > 6) or (y - x < 4)


data = []
for A in range(1, 100):
    if all(f(A, x, y) for x in range(1, 100) for y in range(1, 100)):
        data.append(A)
print(min(data))