def f(A, x):
    return (x in Q) <= (((x in P) == (x in Q)) or (not (x in P) <= (x in A)))


P = [i / 10 for i in range(69 * 10, 91 * 10 + 1)]
Q = [i / 10 for i in range(77 * 10, 114 * 10 + 1)]

A = set()
for x in [i / 10 for i in range(60 * 10, 120 * 10)]:
    if not f(A, x):
        A.add(x)
print(sorted(A))

A = list(A)
for i in range(86, 114):
    print(f"{i}: {A.count(i)}")
print(114 - 91)