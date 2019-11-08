# 메모리 초과
T = int(input())
tiles = [0] + list(map(int, input().split()))
N = tiles[-1]+1
temp = [[0] * 4 for _ in range(T+2)]  # idx, tiles[idx], cnt, gap (현재 타일에서 이전 타일들과의 비교)
array = [[i[:] for i in temp] for _ in range(T+1)]
max_num = 0
for v in range(T+1):
    array[v][0] = []
    for t in range(1, v+1):  # 1 ~ T+2
        array[v][0].append(t-1)  # 타일을 0개부터 T+1까지 가지고 있음
        array[v][t][0] = t-1
        array[v][t][1] += tiles[t-1]
        array[v][t][2] += 1
        array[v][t][3] = tiles[v]-tiles[t-1]
    for idx in array[v][0]:
        pre_idx = array[v][idx+1][0]
        for pdx in array[pre_idx][0]:
            if array[pre_idx][pdx+1][3] == array[v][idx+1][3]:  # 현재 타일과 이전타일중 gap이 같은 것을 더함
                array[v][idx+1][1] += array[pre_idx][pdx+1][1]
                array[v][idx+1][2] += array[pre_idx][pdx+1][2]

        if array[v][idx+1][2] >= 2 and max_num < array[v][idx+1][1] + tiles[v]:  # cnt가 2 이상이고 과거의 타일들을 더한 값 + 현재 타일의 값
            max_num = array[v][idx+1][1] + tiles[v]

print(max_num)
print(array)