# 효율성 13번 통과 x

def solution(stones, k):
    max_idx_in_k, max_value_in_k = get_max_num_in_k(stones, 0, k)
    min_max_num = max_value_in_k

    for i in range(len(stones) - k):
        if stones[i+k] > max_value_in_k:
            max_value_in_k = stones[i+k]
            max_idx_in_k = i+k
        elif i == max_idx_in_k:
            max_idx_in_k, max_value_in_k = get_max_num_in_k(stones, i+1, k)
            min_max_num = min(min_max_num, max_value_in_k)
    return min_max_num


def get_max_num_in_k(stones, now, k):
    max_idx = 0
    max_value = 0
    for i in range(now, now+k):
        if max_value < stones[i]:
            max_value = stones[i]
            max_idx = i
    return max_idx, max_value

dataset = [
    [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3]
]

for stones, k in dataset:
    print(solution(stones, k))