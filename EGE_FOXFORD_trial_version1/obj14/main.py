for x in '0123456789ABCDEFG':
    res = int(f'1B4{x}6', 17) + int(f'1{x}2{x}', 17)
    if res % 19 == 0:
        print(x)
        print(res // 19)
        break
