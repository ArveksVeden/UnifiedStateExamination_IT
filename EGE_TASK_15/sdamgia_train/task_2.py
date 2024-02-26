#  ищем наименьший отрезок A
def f(A, x):
    return (x not in A) <= ((x in P) <= (x not in Q))


P = [i / 10 for i in range(20 * 10, 50 * 10 + 1)]
Q = [i / 10 for i in range(30 * 10, 65 * 10 + 1)]

A = set()
for x in [i / 10 for i in range(10 * 10, 70 * 10 + 1)]:
    if not f(A, x):
        A.add(x)
print(sorted(A))
#  30->50
print(50 - 30)