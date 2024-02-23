def f(A, x):
    return ((x % 3 == 0) <= (x % 11 != 0)) or (x + A >= 80)


data = []
for A in range(1, 1000):
    if all(f(A, x) for x in range(1, 100)):
        data.append(A)
print(min(data))