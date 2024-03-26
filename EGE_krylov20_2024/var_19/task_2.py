def f(x, y, z, w):
    return (not ((x == y) or (x == z))) or w or (not (y <= z))


print('x w y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, w, y, z)
