def f(A, x):
    return (x % A != 0) <= ((x % 21 == 0) <= (x % 14 != 0))


data = []
for A in range(1, 1000):
    if all(f(A, x) for x in range(1, 100)):
        data.append(A)
print(max(data))