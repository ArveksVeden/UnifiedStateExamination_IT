def f(x, y, z, w):
    return (not (y <= (not (z <= w)))) and ((not z) <= ((not w) == x))


print('y w z x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(y, w, z, x)
