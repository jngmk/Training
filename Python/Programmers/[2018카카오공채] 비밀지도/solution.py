def solution(n, arr1, arr2):
    board = [[' '] * n for _ in range(n)]
    arr1 = list(map(make_bin, arr1))
    arr2 = list(map(make_bin, arr2))
    for r in range(n):
        for arr in arr1, arr2:
            len_row = len(arr[r])
            cnt = n - len_row
            row = '0' * cnt + arr[r] if len_row < n else arr[r]

            for i in range(n):
                if row[i] == '0':
                    continue
                else:
                    board[r][i] = '#'
    board = list(map(''.join, board))
    return board


def make_bin(num):
    return bin(num)[2:]

data = [
    [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
    [6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]],
]


for n, arr1, arr2 in data:
    print(solution(n, arr1, arr2))
    # break