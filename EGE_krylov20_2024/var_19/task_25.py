def is_simp(x):
    return all(x % p != 0 for p in range(2, int(x**0.5) + 1))


num = 450_000 + 1
cout = 0

while True:
    divs1 = [p for p in range(2, int(num**0.5) + 1) if num % p == 0]
    divs2 = [num // p for p in divs1 if p**2 != num]
    divs = divs1 + divs2[::-1]

    if len(divs) == 0:
        num += 1
        continue

    if not is_simp(max(divs)):
        print(num, max(divs))
        cout += 1
    num += 1
    if cout == 6:
        break
