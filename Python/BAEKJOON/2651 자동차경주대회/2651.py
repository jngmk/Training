ability = int(input())
drop_by = int(input())
temp = [0]
temp += list(map(int, input().split()))
distances = [sum(temp[:i+1]) for i in range(drop_by+2)]
time = [0]
time += list(map(int, input().split()))
time += [0]
cnt = 0
result = [0] * (drop_by+2)
result[0] = time[0], '', cnt
for v in range(1, drop_by+2):
    temp = []
    for d in range(v):
        if distances[v] - distances[d] <= ability:
            temp.append(d)
    min_time = 10000000
    for t in temp:
        if int(result[t][0]) < min_time:
            min_time = int(result[t][0])
            min_idx = t
    if v == drop_by+1:
        min_road = result[min_idx][1]
    else:
        min_road = result[min_idx][1] + str(v) + ' '
    result[v] = [min_time+time[v], min_road, result[min_idx][2]+1]

if result[-1][2]-1 == 0:
    print(result[-1][0])
    print(result[-1][2] - 1)
else:
    print(result[-1][0])
    print(result[-1][2]-1)
    print(result[-1][1])
