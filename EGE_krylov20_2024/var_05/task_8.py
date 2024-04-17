# 4096 - 32767 + 1
# 1 3 5 7


cout = 0
for i in range(4096, 32767 + 1):
    nope = ['14', '41', '34', '43', '54', '45', '75', '47']
    s = oct(i)[2:]
    if s.count('4') == 2 and all(p not in s for p in nope):
        cout += 1
print(cout)
