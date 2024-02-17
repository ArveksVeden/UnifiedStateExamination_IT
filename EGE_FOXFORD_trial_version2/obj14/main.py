#11031
for x in '0123456789ABCDEFG':
    r = int(f'153{x}4', 16) + int(f'1{x}325', 16)
    if r % 15 == 0:
        print(r / 15)
        break
