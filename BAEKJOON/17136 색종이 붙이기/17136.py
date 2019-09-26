def puzzle(papers, temp1, visited, is_zero, puzzle_cnt):
    global array, min_puzzle
    s, e = visited
    for a in range(s, 10):
        for b in range(e, 10):
            if array[a][b] == 1:
                print(a, b)
                is_zero = False
                for i in range(6):
                    possible = False
                    if papers[i] > 0:
                        if change(a, b, i):
                            possible = True
                            next_paper = papers[:]
                            next_paper[i] -= 1
                            print(next_paper)
                            print(papers)
                            # print(array)
                            puzzle(next_paper, temp2, (a, b), is_zero, puzzle_cnt + 1)
                            for aa, bb in temp1:
                                array[aa][bb] = 1
                        else:
                            continue
                if possible is False:
                    continue

    if is_zero is False and puzzle_cnt == 0:
        min_puzzle = -1

    elif min_puzzle > puzzle_cnt:
        min_puzzle = puzzle_cnt
        return


def change(a, b, size):
    global temp2, array
    temp2 = []
    cnt = 0
    if a + size >= 10 or b + size >= 10:
        return False

    for da in range(size):
        for db in range(size):
            if array[a+da][b+db] == 1:
                cnt += 1
                temp2.append((a+da, b+db))
    if cnt == size * size:
        for aa, bb in temp2:
            array[aa][bb] = -size
        return True


array = [list(map(int, input().split())) for _ in range(10)]
temp2 = []
min_puzzle = 999
puzzle([0, 5, 5, 5, 5, 5], [], (0, 0), True, 0)

print(min_puzzle)
