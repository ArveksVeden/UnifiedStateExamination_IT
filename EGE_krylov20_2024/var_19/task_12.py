s = '1' + '2' * 70

while '12' in s or '1' in s:
    if '12' in s:
        s = s.replace('12', '221', 1)
    else:
        if '1' in s:
            s = s.replace('1', '2', 1)
print(s.count('2'))
