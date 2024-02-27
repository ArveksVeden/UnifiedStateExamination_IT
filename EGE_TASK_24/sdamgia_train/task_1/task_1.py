f = open("24.txt")
s = f.read()

max_len = 0
for i in range(len(s) - 1):
    cout = 0
    c_cout = 0
    d_cout = 0
    for j in range(i, len(s) - 1):
        cout += 1
        if s[j] == 'D':
            d_cout += 1
        elif s[j] == 'C':
            c_cout += 1
        if d_cout > 2 or c_cout > 2:
            if cout - 1 > max_len:
                max_len = cout - 1
            break
print(max_len)