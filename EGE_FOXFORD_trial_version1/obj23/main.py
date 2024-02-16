def k(a, b):
    if a == b:
        return 1
    if a > b or a == 21:
        return 0
    return k(a + 1, b) + k(a * 2, b)
print(k(1, 18) * k(18, 49))
