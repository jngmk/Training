# 효율성 통과 X

from heapq import heappush, heappop


def solution(food_times, k):
    length = len(food_times)
    visited = [0] * length
    h = []
    for i in range(length):
        time = food_times[i]
        heappush(h, [time, i])

    prev_time = 0
    num = length
    cnt = 0
    while h:
        time, i = heappop(h)
        print('time, i ', time, i, visited)
        repeat = time - prev_time
        cnt += num * repeat
        if cnt > k:
            print('check', cnt - k)
            idx = 1
            for _ in range(repeat):
                for j in range(length-1, -1, -1):
                    if visited[j]:
                        continue
                    if idx == cnt - k:
                        return j+1
                    idx += 1
            # break
        visited[i] = 1
        num -= 1
        prev_time = time
        print(cnt, num)
    return -1


dataset = [
    [[3, 1, 2, 1, 1, 6, 7, 1], 18]
]

for food_times, k in dataset:
    print(solution(food_times, k))