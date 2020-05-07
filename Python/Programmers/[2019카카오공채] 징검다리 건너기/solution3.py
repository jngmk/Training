# segtree!! 참고

from sys import maxsize
INT_MIN = -maxsize

def construct_segment_tree(a: list, n: int):
    global segtree

    for i in range(n):
        segtree[n + i] = a[i]

    for i in range(n - 1, 0, -1):
        segtree[i] = max(segtree[2 * i], segtree[2 * i + 1])


def range_query(left: int, right: int, n: int) -> int:
    global segtree

    left += n
    right += n

    ma = INT_MIN
    while left < right:
        if left & 1:
            ma = max(ma, segtree[left])
            left += 1
        if right & 1:
            right -= 1
            ma = max(ma, segtree[right])
        left //= 2
        right //= 2

    return ma


def solution(stones, k):

    global segtree

    n = len(stones)
    segtree = [0] * (2 * n)
    construct_segment_tree(stones, n)
    part_max = []

    for i in range(len(stones)):
        if i+k > n:
            break
        part_max.append(range_query(i, i+k, n))

    ans = min(part_max)

    return ans