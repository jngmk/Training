from itertools import permutations


def solution(n, weak, dist):
    answer = -1
    length = len(weak)
    dist = list(reversed(sorted(dist)))
    for d_idx in range(1, len(dist)+1):
        for i in range(length):
            for group in permutations(dist[:d_idx], d_idx):
                start = weak[i]
                visited = [0] * length
                idx = i
                for p in group:
                    visited[idx] = 1
                    while True:
                        if sum(visited) == length:
                            return d_idx
                        idx += 1
                        idx %= length
                        distance = weak[idx] - start
                        if distance < 0: distance += n
                        if distance <= p:
                            visited[idx] = 1
                        else:
                            start = weak[idx]
                            break
    return answer


dataset = [
    [12, [1, 5, 6, 10], [1, 2, 3, 4]],
    [12, [1, 3, 4, 9, 10], [3, 5, 7]]
]

for n, weak, dist in dataset:
    print(solution(n, weak, dist))