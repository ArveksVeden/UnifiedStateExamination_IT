x = 1414562
divs1 = [p for p in range(1, int(x**0.5) + 1) if x % p == 0]
divs2 = [x // p for p in divs1 if p**2 != x]
divs = divs1 + divs2[::-1]
