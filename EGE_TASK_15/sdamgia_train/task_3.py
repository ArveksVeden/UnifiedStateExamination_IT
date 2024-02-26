def f(A, x):
    return (x in P) <= (not (x in Q) <= (not ((x in P) and not (x in A))))


P = [i / 10 for i in range(19 * 10, 84 * 10 + 1)]
Q = [i / 10 for i in range(4 * 10, 51 * 10 + 1)]

A = set()
for x in [i / 10 for i in range(1 * 10, 90 * 10 + 1)]:
    if not f(A, x):
        A.add(x)
print(sorted(A))

A = list(A)
print(84 - 51)