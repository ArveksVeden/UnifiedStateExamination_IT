from fnmatch import *

num = 0
i = 1
while True:
    num = i * 123
    if num > 10**8:
        break
    if fnmatch(f'{num}', '32*823'):
        print(num, num // 123)

    i += 1
