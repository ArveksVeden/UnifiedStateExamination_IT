def f(A, x):
    return ((x in P) == (x in Q)) <= (not (x in A))


P = [i / 10 for i in range(5 * 10, 30 * 10 + 1)]
Q = [i / 10 for i in range(14 * 10, 23 * 10 + 1)]

A = set([i / 10 for i in range(4 * 10, 35 * 10)])
for x in [i / 10 for i in range(4 * 10, 35 * 10)]:
    if not f(A, x):
        A.remove(x)
print(sorted(A))

A = list(A)
for i in range(4, 35):
    print(f"{i}: {A.count(i)}")

print(14 - 5)