f = open('17/17var02.txt')
data = [int(p[:-1]) for p in f]

max_100 = 0
for i in data:
    if len(str(i)) >= 3:
        if str(i)[-3:] == '100':
            if i > max_100:
                max_100 = i

nope = []
for i in range(2, len(data)):
    el1 = data[i]
    el2 = data[i - 1]
    el3 = data[i - 2]
    if len(str(el1)) == 3 and len(str(el2)) == 3 and len(str(el3)) != 3 or\
    len(str(el1)) != 3 and len(str(el2)) == 3 and len(str(el3)) == 3 or\
    len(str(el1)) == 3 and len(str(el2)) != 3 and len(str(el3)) == 3:
        if (el1 + el2 + el3) <= max_100:
            nope.append(el1 + el2 + el3)
print(len(nope), max(nope))
