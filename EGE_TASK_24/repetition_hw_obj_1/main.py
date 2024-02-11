f = open("nope.txt")
s = f.read()
cur_cout = 0
max_len = 0
cur_res = ''
max_res = ''
flag = False
for i in s:
    if i == 'A' and not flag:
        flag = True
        cur_cout += 1
        cur_res += i
    if i == 'A' and flag:
        cur_cout = 1
        cur_res = i
        continue
    if flag and i != "Z":
        cur_cout += 1
        cur_res += i
    if flag and i == 'Z':
        cur_res += i
        cur_cout += 1
        flag = False
        if cur_cout > max_len:
            max_res = cur_res
            cur_res = ''
            max_len = cur_cout
            cur_cout = 0
print(max_len)
print(max_res)
