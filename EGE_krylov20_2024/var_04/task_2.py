def f(x, y, z, w):
    return (not (w <= x)) or ((not z) <= (not y)) or z


print('y z x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(y, z, x, w)
