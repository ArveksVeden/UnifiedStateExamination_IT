for x in '0123456789ABCDEFGHIJKLMNOPQR':
    res = int(f'1{x}1{x}1{x}1{x}1', 23) + int(f'20{x}24', 23) + int(f'1{x}235', 23)
    if res % 22 == 0:
        print(res / 22)
        break
