def f(x, y, z, w):
    return not (y <= x) or (y == w) or z


print('z y w x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(z, y, w, x)
