def f(x, y, z, w):
    return y and (x <= w) and ((not x) <= ((not w) == z))


print('x z y w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, z, y, w)
