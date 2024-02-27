f = open('24.txt')
data = [p.strip() for p in f]

cout = []
for i in data:
    cout.append(i.count('G'))

res_str = data[cout.index(min(cout))]

max_cout = 0
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if res_str.count(i) > max_cout:
        max_cout = res_str.count(i)
    print(f"{i}: {res_str.count(i)}")
print(max_cout)