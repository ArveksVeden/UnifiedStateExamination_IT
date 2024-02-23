def f(A, x):
    return ((x in A) <= (x**2 <= 25)) and ((x**2 <= 9) <= (x in A))


data = []
for a in range(-100, 100):
    for b in range(a, 100):
        A = range(a, b + 1)
        if all(f(A, x) for x in range(-100, 100)):
            data.append(b - a)
print(min(data))