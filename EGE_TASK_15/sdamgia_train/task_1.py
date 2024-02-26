#ищем наибольший отрезок A
def f(A, x):
    return ((x in Q) <= (x in P)) <= (x not in A)


P = [i / 10 for i in range(3 * 10, 38 * 10 + 1)]
Q = [i / 10 for i in range(21 * 10, 57 * 10 + 1)]

A = set(i / 10 for i in range(2 * 10, 60 * 10 + 1))

for x in [i / 10 for i in range(2 * 10, 60 * 10 + 1)]:
    if not f(A, x):
        A.remove(x)
print(sorted(A))
print(57 - 38)