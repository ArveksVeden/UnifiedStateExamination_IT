f = open('24.txt')
s = f.read()

a = s.split('A')
t = 3
kmax = 0
k = 0

for i in range(0, t + 1):
    k += len(a[i])
    if i != t:
        k += 1

for i in range(t + 1, len(a)):
    kmax = max(k, kmax)
    k -= len(a[i-t-1])
    k -= 1
    k += 1
    k += len(a[i])
print(max(kmax, k))
