f = open('24.txt')
s = f.read()

a = s.split('V')
kmin = 10**10
k = 0
t = 120

for i in range(1, t):
    k += len(a[i])
    k += 1
k += 1

for i in range(t, len(a) - 1):
    kmin = min(kmin, k)
    k -= len(a[i-t+1])
    k -= 1
    k += 1
    k += len(a[i])

print(min(kmin, k))
