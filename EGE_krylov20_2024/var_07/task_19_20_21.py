from functools import lru_cache


def moves(h):
    return [h + 1, h*2]


@lru_cache(None)
def game(h):
    if h >= 153: return 'W'
    if any(game(i) == 'W' for i in moves(h)): return 'P1'
    if all(game(i) == 'P1' for i in moves(h)): return 'B1'
    if any(game(i) == 'B1' for i in moves(h)): return 'P2'
    if all(game(i) == 'P1' or game(i) == 'P2' for i in moves(h)): return 'B2'


for s in range(1, 152 + 1):
    if game(s) == 'B2':
        print(s, game(s))
