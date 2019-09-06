N, M = map(int, input().split())
street = [list(map(int, input().split())) for _ in range(N)]
c_range = []
danger_zone = N * M
cameras = []
di = [[], [[1], [2], [3], [4]], [[1, 3], [2, 4]], [[1, 2], [2, 3], [3, 4], [4, 1]], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], [[1, 2, 3, 4]]]
safe_zone = 0
da = [0, -1, 0, 1, 0]
db = [0, 0, 1, 0, -1]


def rotation(k, now, temp_cnt, cam_range):
    global safe_zone
    if k == len(cameras):
        if safe_zone < temp_cnt:
            safe_zone = temp_cnt
    else:
        for c in range(now+1, len(cameras)):
            a, b = cameras[c]
            c_num = street[a][b]
            for direction in di[c_num]:
                cnt = 0
                temp_range = []
                for d in direction:
                    aa, bb = a, b
                    while True:
                        ra = aa + da[d]
                        rb = bb + db[d]
                        if ra < 0 or ra > N-1 or rb < 0 or rb > M-1 or street[ra][rb] == 6:
                            break
                        if (ra, rb) not in cam_range:
                            cnt += 1
                            temp_range.append((ra, rb))
                            aa = aa + da[d]
                            bb = bb + db[d]
                        else:
                            aa = aa + da[d]
                            bb = bb + db[d]

                rotation(k+1, c, temp_cnt+cnt, cam_range+temp_range)


for i in range(N):
    for j in range(M):
        if 0 < street[i][j] < 6:
            cameras.append((i, j))
            c_range.append((i, j))
            danger_zone -= 1
        elif street[i][j] == 6:
            danger_zone -= 1

rotation(0, -1,  0, c_range)
danger_zone = danger_zone - safe_zone
print(danger_zone)
