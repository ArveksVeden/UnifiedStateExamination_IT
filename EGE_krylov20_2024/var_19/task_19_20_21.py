from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a * b >= 144: return 'W'
    if any(game(i) == 'W' for i in moves(h)): return 'P1'
    if all(game(i) == 'P1' for i in moves(h)): return 'B1'
    if any(game(i) == 'B1' for i in moves(h)): return 'P2'
    if all(game(i) == 'P1' or game(i) == 'P2' for i in moves(h)): return 'B2'


for s in range(1, 142+1):
    h = 1, s

    if game(h) == 'B2':
        print(s, game(h))
