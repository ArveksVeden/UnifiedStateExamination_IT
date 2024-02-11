f = open('nope.txt')
s = f.read()
glas = 'AEO'
sogl = 'BCD'
cur_cout = 0
max_len = 0
cur_res = ''
max_res = ''
flag = False
for i in range(len(s)):
    if s[i] in glas and not flag:
        flag = True
        continue
    if s[i] in sogl and flag:
        cur_cout += 1
        cur_res += s[i-1] + s[i]
        flag = False
        continue
    if s[i] in glas and flag:
        if cur_cout > max_len:
            max_len = cur_cout
            max_res = cur_res
        cur_res = ''
        cur_cout = 0
        continue
    if s[i] in sogl and not flag:
        if cur_cout > max_len:
            max_len = cur_cout
            max_res = cur_res
        cur_res = ''
        cur_cout = 0
        continue
print(max_len)
print(max_res)
