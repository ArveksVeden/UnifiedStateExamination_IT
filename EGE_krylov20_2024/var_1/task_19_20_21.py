from functools import lru_cache


def moves(h):
    return [h + 1, h + 4, h * 3]


@lru_cache(None)
def game(h):
    if h >= 202: return 'W'
    if any(game(i) == 'W' for i in moves(h)): return 'P1'
    if all(game(i) == 'P1' for i in moves(h)): return 'B1'
    if any(game(i) == 'B1' for i in moves(h)): return 'P2'
    if all(game(i) == 'P1' or game(i) == 'P2' for i in moves(h)): return 'B2'


for h in range(1, 202):
    if game(h) == 'B2':
        print(h, game(h))
