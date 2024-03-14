from functools import lru_cache

# 19 ans: 25
# 20 ans: 66 69
# 21 ans: 62 70


def moves(h):
    a, b = h
    return (a + 4, b), (a, b + 4), (a * 3, b), (a, b * 3)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 231: return 'W'
    if any(game(i) == 'W' for i in moves(h)): return 'P1'
    if all(game(i) == 'P1' for i in moves(h)): return 'B1'
    if any(game(i) == 'B1' for i in moves(h)): return 'P2'
    if all(game(i) == 'P1' or game(i) == 'P2' for i in moves(h)): return 'B2'


for i in range(1, 230):
    h = 10, i
    if game(h) == 'B2':
        print(i, game(h))