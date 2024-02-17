s = '8' * 244 + '4' * 22
while '4444' in s or '8888' in s:
    if '4444' in s:
        s = s.replace('4444', '8', 1)
    else:
        s = s.replace('8888', '4', 1)
print(s)
