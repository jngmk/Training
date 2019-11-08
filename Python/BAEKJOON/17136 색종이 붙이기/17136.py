def puzzle(papers, visited, puzzle_cnt):
    global min_puzzle, impossible
    s, e = visited
    for a in range(s, 10):
        for b in range(10):
            if array[a][b] == 1:
                impossible = True
                for i in range(5, 0, -1):
                    if papers[i] > 0 and change(a, b, i):
                        papers[i] -= 1
                        for aa in range(a, a+i):
                            for bb in range(b, b+i):
                                array[aa][bb] = 0
                        puzzle(papers, (a, b), puzzle_cnt + 1)
                        for aa in range(a, a+i):
                            for bb in range(b, b+i):
                                array[aa][bb] = 1
                        papers[i] += 1
                return
    if min_puzzle > puzzle_cnt:
        min_puzzle = puzzle_cnt
    return


def change(aa, bb, size):
    if aa + size > 10 or bb + size > 10:
        return False

    for da in range(size):
        for db in range(size):
            if array[aa + da][bb + db] != 1:
                return False

    return True


array = [list(map(int, input().split())) for _ in range(10)]
min_puzzle = 999
impossible = False
puzzle([0, 5, 5, 5, 5, 5], (0, 0), 0)
if min_puzzle == 999:
    min_puzzle = -1

print(min_puzzle)
