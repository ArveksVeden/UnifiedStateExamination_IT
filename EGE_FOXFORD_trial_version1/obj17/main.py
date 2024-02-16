f = open('17.txt')
data = [int(p[:-1]) for p in f]
min_el = 1000000
for i in data:
    if i % 10 == 5 and i < min_el:
        min_el = i
min_el = min_el**2

res = []
cout = 0
for i in range(1, len(data)):
    if (data[i] % 10 == 5 and data[i - 1] % 10 != 5) or \
       (data[i] % 10 != 5 and data[i - 1] % 10 == 5):
        qv = (data[i] + data[i - 1])**2
        if qv >= min_el:
            res.append(qv)
            cout += 1
print(cout)
print(max(res))
