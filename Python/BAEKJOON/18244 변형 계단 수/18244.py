def find_pattern(k, pattern, prev_pattern, last_num):
    global patterns
    if k == N:
        patterns.append(pattern)
        return

    if (prev_pattern == 0 or prev_pattern == 3 or prev_pattern == 4) and k <= N-2:
        find_pattern(k+2, pattern+[last_num+1, last_num+2], 1, last_num+2)

    if (prev_pattern == 0 or prev_pattern == 3 or prev_pattern == 4) and k <= N-1:
        find_pattern(k+1, pattern+[last_num+1], 2, last_num+1)

    if (prev_pattern == 0 or prev_pattern == 1 or prev_pattern == 2) and k <= N-1:
        find_pattern(k+1, pattern+[last_num-1], 3, last_num-1)

    if (prev_pattern == 0 or prev_pattern == 1 or prev_pattern == 2) and k <= N-2:
        find_pattern(k+2, pattern+[last_num-1, last_num-2], 4, last_num-2)


N = int(input())
patterns = []
find_pattern(1, [], 0, 0)
print(patterns[:len(patterns)//2])
cnt = 0
for pattern in patterns[:len(patterns)//2]:
    print([0]+pattern)
    max_num = max(pattern+[0]); min_num = min(pattern+[0])
    cnt += (10 - (max_num - min_num))
    # print('find', 10 - (max_num - min_num))

print(cnt)
# print(10*len(patterns) - cnt)