def f(x, y, z, w):
    return (x <= (not w)) and (y <= x) and z
print('z x y w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(z, x, y, w)
