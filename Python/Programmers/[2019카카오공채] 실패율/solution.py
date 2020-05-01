from heapq import heappush, heappop


def solution(N, stages):
    answer = []
    h = []
    failure = [[0, 0] for _ in range(N + 2)]

    for stage in stages:
        failure[stage][0] += 1
    failure[N + 1][1] = failure[N + 1][0]

    for i in range(N + 1, 1, -1):
        failure[i - 1][1] = failure[i][1] + failure[i - 1][0]
        failure_rate = -(failure[i - 1][0] / failure[i - 1][1]) if failure[i - 1][1] != 0 else 0
        heappush(h, [failure_rate, i - 1])

    while h:
        answer.append(heappop(h)[1])

    return answer


data = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3]],
    [4, [4,4,4,4,4]],
]


for N, stages in data:
    print(solution(N, stages))
    break