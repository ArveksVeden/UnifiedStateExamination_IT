for n in range(1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r
        r = r[:-1] + '1'
    else:
        r = '1' + r
        r = r[:-2] + '11'
    r = int(r, 2)
    if r > 85:
        print(n)
        break
