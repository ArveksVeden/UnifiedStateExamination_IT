#1513
cout = 0
data = []
data1 = []

for i in range(1513, 10**10):
    n = i * 2021
    s = str(n)
    if s[::-1][0] == '7':
        _ = s[::-1][-3:][::-1]
        if _[0] == '3' and _[2] == '5':
            _ = s[3:]
            if _[:3] == '919':
                print(n, n % 2021)
                data.append(n)
                data1.append(n // 2021)
                cout += 1
                print(cout)
                if cout == 3:
                    break
print("data | data1")
for i in range(len(data)):
    print(f"{data[i]} | {data1[i]}")
