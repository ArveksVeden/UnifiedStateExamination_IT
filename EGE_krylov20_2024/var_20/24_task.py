f = open('24.txt')
s = f.read()


cur_len = 1
max_len = 1
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        cur_len += 1
        continue
    else:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 1
print(max_len)
