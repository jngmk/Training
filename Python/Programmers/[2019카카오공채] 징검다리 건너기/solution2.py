# 통과

def check(stones, num, k):
    impossible = 0
    for stone in stones:
        if stone < num:
            impossible += 1
        else:
            impossible = 0
        if impossible >= k:
            return False
    return True


def solution(stones, k):
    answer = 1
    left = 1
    right = max(stones) + 1
    while left < right:
        mid = (left + right) // 2
        if check(stones, mid, k):
            answer = mid
            left = mid + 1
        else:
            right = mid

    return answer


dataset = [
    [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3]
]

for stones, k in dataset:
    print(solution(stones, k))