# 시간초과
from pprint import pprint

T = int(input())
tiles = [0] + list(map(int, input().split()))
array = []
for i in range(T+1):  # idx, tiles[idx], cnt, gap (현재 타일에서 이전 타일들과의 비교)
    array.append([])
    for j in range(i+1):
        array[i].append([0, 0, 0, 0])

max_num = 0
for v in range(T+1):
    array[v][0] = []
    for t in range(1, v+1):  # 1 ~ T+2 # 타일을 0개부터 T+1까지 가지고 있음
        array[v][0].append(tiles[v] - tiles[t-1])  # 타일을 0개부터 T+1까지 가지고 있음
        array[v][t][0] = t-1
        array[v][t][1] += tiles[t-1]
        array[v][t][2] += 1
        array[v][t][3] = tiles[v] - tiles[t-1]

    for idx in range(1, len(array[v])):
        pre_idx = array[v][idx][0]
        for pdx in range(1, pre_idx+1):
            if array[v][idx][3] not in array[pre_idx][0]:
                break
            if array[pre_idx][pdx][3] == array[v][idx][3]:  # 현재 타일과 이전타일중 gap이 같은 것을 더함
                array[v][idx][1] += array[pre_idx][pdx][1]
                array[v][idx][2] += array[pre_idx][pdx][2]

        if array[v][idx][2] >= 2 and max_num < array[v][idx][1] + tiles[v]:  # cnt가 2 이상이고 과거의 타일들을 더한 값 + 현재 타일의 값
            max_num = array[v][idx][1] + tiles[v]

pprint(array)
print(max_num)
