#задание 17
#ans:
#881
#348419556
f = open('17.txt')
d = [int(p) for p in f.readlines()]

cout = 0
min_el = 10000000
for i in d:
    n = i
    if abs(n) % 10 == 4 and n < min_el:
        min_el = n
min_el = abs(min_el)
result = []

for i in range(len(d) - 1):
    if (abs(d[i]) % 10 == 4 and abs(d[i + 1]) % 10 != 4)\
       or (abs(d[i]) % 10 != 4 and abs(d[i + 1]) % 10 == 4):
        if (d[i] + d[i + 1])**2 >= min_el:
            cout += 1
            result.append((d[i] + d[i + 1])**2)
print(cout)
print(max(result))
print(len(result))
