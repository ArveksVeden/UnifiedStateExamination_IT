#задание 23
def k(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    else:
        return k(a - 3, b) + k(a // 2, b)
print(k(73, 13) * k(13, 2))
