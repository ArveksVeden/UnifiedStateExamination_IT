for n in range(3, 10_000 + 1):
    s = '1' + '2' * n

    while '12' in s or '5522' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '55', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '5522' in s:
            s = s.replace('5522', '21', 1)
    cout = 0
    for i in s:
        cout += int(i)
    if cout == 142:
        print(n)
        break
