# ans:

for n in range(3, 10_000 + 1):
    s = '1' + '2' * n

    while '12' in s or '3322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)

    cout = 0
    for i in s:
        cout += int(i)
    if cout == 218:
        print(n)
        break
