#  решение задачи 19 - где петя затупил первым ходом => ваня побеждает своим первым

from functools import lru_cache

def moves(h):
    #  a, b - 2 множества => 2 кучи
    a, b = h
    #  возвращаем все возможные ходы с 2 кучами
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b =  h
    #условие победы - a + b >= 83
    if a + b >= 83: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    #  меняем all на any для задачи (где петя ошибся, после чего ваня выигрывает)
    if any(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 200):
    #  формируем h и передаем в виде параметра
    h = 9, s
    if game(h) == 'B1':
        print(s, game(h))
