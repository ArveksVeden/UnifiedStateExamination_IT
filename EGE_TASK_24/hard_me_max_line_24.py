f = open('24.txt')
s = f.read()

a = s.split('A')

t = 350
k = 0
kmax = 0

for i in range(0, t + 1):
    k += len(a[i])
    if i != t:
        k += 1

for i in range(t + 1, len(a)):
    kmax = max(kmax, k)

    k -= len(a[i-t-1])
    k -= 1
    k += 1
    k += len(a[i])

kmax = max(kmax, k)
print(kmax)
