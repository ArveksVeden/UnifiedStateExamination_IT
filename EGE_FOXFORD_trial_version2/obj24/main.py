#задание 24
#ord | chr
#ans: 55
f = open('24.txt')
s = f.read()
glas = 'AE'
sogl = 'BCD'

cur_len = 0
max_len = 0

flag = False
for i in range(len(s) - 1):
    if s[i] in glas and not flag:
        flag = True
        continue
    if flag and s[i] in sogl:
        flag = False
        cur_len += 1
        continue
    if flag and s[i] in glas:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 0
        continue
    if not flag and s[i] in sogl:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 0
        continue
print(max_len)
