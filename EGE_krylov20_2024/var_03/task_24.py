f = open('24.txt')
s = f.read()

a = s.split('A')
t = 500
k = 0
kmin = 10**10

for i in range(1, t):
    k += len(a[i])
    k += 1
k += 1

for i in range(t, len(a) - 1):
    kmin = min(k, kmin)
    k -= 1
    k -= len(a[i-t+1])
    k += len(a[i])
    k += 1

print(min(k, kmin))
