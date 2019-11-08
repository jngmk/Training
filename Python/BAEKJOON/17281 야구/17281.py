from itertools import permutations


def inning_get_score():
    global i, score
    for inning in innings:
        p, q, r = 0, 0, 0
        out = 0
        while out < 3:
            if inning[order[i]] == 0:
                out += 1
            elif inning[order[i]] == 1:
                score += p
                p, q, r = q, r, 1
            elif inning[order[i]] == 2:
                score += p + q
                p, q, r = r, 1, 0
            elif inning[order[i]] == 3:
                score += p + q + r
                p, q, r = 1, 0, 0
            else:
                score += p + q + r + 1
                p, q, r = 0, 0, 0
            i = (i + 1) % 9


N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
result = 0
orders = list(permutations([1, 2, 3, 4, 5, 6, 7, 8], 8))
for order in orders:
    order = list(order)
    order[3:0] = [0]
    i = 0
    score = 0
    inning_get_score()
    result = max(result, score)
print(result)
