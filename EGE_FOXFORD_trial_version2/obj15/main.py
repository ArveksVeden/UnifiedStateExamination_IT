#задание 15
#ans: 16
def f(A, x, y):
    return (x + y <= 25) or (x <= y + 5) or (x >= A)
data = []
for A in range(1, 1000):
    if all(f(A, x, y) for x in range(1, 100) for y in range(1, 100)):
        data.append(A)
print(max(data))
