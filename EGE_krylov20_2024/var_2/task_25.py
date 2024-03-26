from fnmatch import *

num = 0
i = 1

while True:
    num = i * 12007
    if num > 10**10 + 1:
        break
    if fnmatch(str(num), '9*?001?1'):
        print(num, num / 12007)
    i += 1
