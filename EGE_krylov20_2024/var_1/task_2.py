# ans: xwzy

def f(x, y, z, w):
    return (not (x <= y)) or (x == z) or w


print('x w z y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f(x, y, z, w):
                    print(x, w, z, y)
