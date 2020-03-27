N, K = map(int, input().split())
cnt = 0

# 2

def find_y_cnt(k, n, num):
    global y_cnt
    if k >= y:
        if num % N == 0:
            y_cnt += 1
            # print(num, y_cnt)
        return

    for nn in range(n+1, leny):
        # print(n, nn)
        find_y_cnt(k+1, nn, num + group_y[nn])


print(cnt % 1000000007)
