f = open('24/24var02.txt')
s = f.read()

data = [p for p in range(len(s)) if s[p] == 'A']
print(max(data[i + 349] - data[i] + 1 for i in range(len(data) - 349)))
