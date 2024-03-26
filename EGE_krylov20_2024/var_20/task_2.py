def f(x, y, z, w):
    return (not ((x == y) or (x == w))) or z or (not (y <= w))


print('w y x z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(w, y, x, z)
