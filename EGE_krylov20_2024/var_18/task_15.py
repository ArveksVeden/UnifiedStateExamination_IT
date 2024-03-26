def f(A, x, y):
    return (x >= A) or (y >= A) or (x*y <= 270)


nope = []
for A in range(100000):
    if all(f(A, x, y) for x in range(200) for y in range(200)):
        nope.append(A)
print(max(nope))
