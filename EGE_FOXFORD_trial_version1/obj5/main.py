for n in range(1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r[::-1] + '01'
        r = r[::-1]
        r = r[:-1] + '1'
    else:
        r = r[::-1] + '1'
        r = r[::-1]
        r = r[:-2] + '10'
    r = int(r, 2)
    if r > 60:
        print(n)
        break
