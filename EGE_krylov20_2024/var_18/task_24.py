f = open('24.txt')
s = f.read()

for i in '0123456789':
    flag = False
    k = 1
    while True:
        c = i * k
        if c not in s:
            print(i, c[:-1])
            break
        else:
            k += 1
