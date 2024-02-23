def f(A, x):
    return (A % 11 == 0) and \
    ((870 % x  == 0) <= ((A % x != 0) <= (1980 % x != 0)))


cout = 0
for A in range(1, 1001):
    if all(f(A, x) for x in range(1, 100)):
        cout += 1
print(cout)