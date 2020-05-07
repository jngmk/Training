# 실패

def solution(stones, k):
    answer = 0
    next_stones = [i+1 for i in range(len(stones)+1)]
    e = len(stones)
    now = 0
    while True:
        next = next_stones[now]
        # print(stones, next_stones)
        # print(now, next)
        if next == e+1:
            answer += 1
            now = 0
            continue
        if next - now > k: break
        stones[next-1] -= 1
        if stones[next-1] == 0:
            next_stones[now] = next_stones[next]
        now = next
    return answer


dataset = [
    [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3]
]

for stones, k in dataset:
    print(solution(stones, k))