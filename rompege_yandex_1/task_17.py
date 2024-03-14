# ans: 610 -123157359

f = open('17.txt')
data = [int(p[:-1]) for p in f]
nope = []

cout = 0
for i in range(2, len(data) - 3):
    pr_s = data[i - 1] + data[i - 2]
    cur_s = data[i] + data[i + 1]
    af_s = data[i + 2] + data[i + 3]
    if pr_s > 0 and cur_s > 0 and af_s > 0:
        if cur_s > pr_s and cur_s > af_s:
            cout += 1
            nope.append(data[i] * data[i + 1])
print(cout, min(nope))