def f(x, y, z, w):
    return (x <= z) and (not (w <= y)) and (not y)
print('x w z y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, w, z, y)
