f = open('17/17var01.txt')
data = [int(p[:-1]) for p in f]

min_el = 10000
for i in data:
    if str(i)[-2:] == '25':
        if i < min_el:
            min_el = i
print(min_el)

res = []
for i in range(2, len(data)):
    if len(str(data[i])) == 2 and len(str(data[i-1])) != 2 and len(str(data[i-2])) != 2 or \
    len(str(data[i])) != 2 and len(str(data[i-1])) == 2 and len(str(data[i-2])) != 2 or \
    len(str(data[i])) != 2 and len(str(data[i-1])) != 2 and len(str(data[i-2])) == 2:
        if data[i] + data[i-1] + data[i-2] < min_el:
            res.append(data[i] + data[i-1] + data[i-2])
print(len(res), max(res))