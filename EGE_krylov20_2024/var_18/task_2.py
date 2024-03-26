def f(x, y, z, w):
    return (w == (not y) or (w == (not z))) and x and (y <= z)


print('x w y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, w, y, z)
