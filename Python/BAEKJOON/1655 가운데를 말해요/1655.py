from heapq import heappop, heappush

N = int(input())
max_h, min_h = [], []
max_h_length, min_h_length = 0, 0
median = 0
n = 1
for _ in range(N):
    v = int(input())
    if n == 1: median = v
    else:
        if v >= median: heappush(max_h, v); max_h_length += 1
        else: heappush(min_h, -v); min_h_length += 1

        # 짝수개일 때
        if n % 2 == 0:
            if min_h_length > max_h_length:
                heappush(max_h, median); max_h_length += 1
                median = -heappop(min_h); min_h_length -= 1
        # 홀수개일 때
        else:
            if min_h_length < max_h_length:
                heappush(min_h, -median); min_h_length += 1
                median = heappop(max_h); max_h_length -= 1
    print(median)
    n += 1
