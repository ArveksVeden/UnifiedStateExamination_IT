def f(A, x, y):
    return (x < A) and (y < A) and (x*y > 1200)


nope = []
for A in range(10000):
    if all(not f(A, x, y) for x in range(200) for y in range(200)):
        nope.append(A)
print(max(nope))
