# 효율성 통과 x

from heapq import heappush, heappop


def build_segtree(length):
    global segtree

    num = 1
    cnt = 0
    while num < length:
        cnt += 1
        num <<= 1
    n = 2 ** cnt

    segtree = [0] * n * 2
    return n


def update_segtree(i):
    global segtree

    segtree[i] = 1
    while i > 1:
        segtree[i//2] += 1
        i //= 2


def get_value(left, right):
    global segtree
    total = 0
    while left < right:
        if left & 1:
            total += segtree[left]
            left += 1
        left //= 2
        if not right & 1:
            total += segtree[right]
            right -= 1
        right //= 2
    if left == right:
        total += segtree[right]
    return total


def solution(food_times, k):
    global segtree

    length = len(food_times)
    n = build_segtree(length)


    rotate_order = [i+1 for i in range(length)]
    h = []
    for i in range(length):
        time = food_times[i]
        heappush(h, [time, i])

    prev_time = 0
    while h:
        time, i = heappop(h)
        print('time, i', time, i)
        cnt = time - prev_time
        print('cnt', cnt)
        update_order = rotate_order * cnt
        print(update_order, k)
        if len(update_order) - 1 >= k:
            return update_order[k]
        k -= len(update_order)


        update_segtree(i+n)
        print('segtree', segtree, rotate_order)
        pop_num = get_value(n, n+i-1)
        print('pop num', pop_num)
        rotate_order.pop(i-pop_num)
        prev_time = time
        print()

    return -1


dataset = [
    [[3, 1, 2, 1, 1, 6, 7, 1], 18]
]

for food_times, k in dataset:
    print(solution(food_times, k))