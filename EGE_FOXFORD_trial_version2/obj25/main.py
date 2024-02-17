#задание 25
#1 ? 3124 * 6
#ans:
#1031243286 520042
#1131245976 570472
count = 0
i = 0
while i < 10**10:
    i += 1983
    s = str(i)
    if len(s) >= 7:
        if s[0] == '1':
            if s[2:][:4] == '3124':
                if s[-1] == '6':
                    print(i, i // 1983)
                    count += 1
                    if count == 2:
                         break
