def triangle(n, m, k):
    return n + m > k and n + k > m and k + m > n


def f(A, x):
    return not ((triangle(x, 11, 18) == (not (max(x, 5) > 15))) and triangle(x, A, 5))


nope = []
for A in range(1, 100):
    if all(f(A, x) for x in range(1, 100000)):
        nope.append(A)
print(max(nope))
