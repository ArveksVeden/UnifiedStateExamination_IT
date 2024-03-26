f = open('24/24var01.txt')
s = f.read()

data = [p for p in range(len(s)) if s[p] == 'A']
print(min(data[i + 2023] - data[i] + 1 for i in range(len(data) - 2023)))
