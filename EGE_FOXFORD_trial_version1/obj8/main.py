import itertools
#4096-32767
data = [''.join(p) for p in itertools.product('0246', repeat = 2)]
cout = 0
for i in range(4096, 32768):
    flag = False
    s = oct(i)[2:]
    if s.count('3') == 1:
        for j in data:
            if j in s:
                flag = True
                break
        if not flag:
            cout += 1
print(cout)
