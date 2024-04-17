from fnmatch import *

num = 0
i = 1

while True:
    num = i * 5171
    if num > 10**8:
        break
    if fnmatch(f'{num}', '?19*8?3'):
        print(num, num / 5171)
    i += 1
