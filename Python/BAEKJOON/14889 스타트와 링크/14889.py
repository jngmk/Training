def make_team(k, now, temp):
    global team1, team2
    if k == N//2:
        team1.append(temp)
        temp2 = []
        for i in range(N):
            if i in temp:
                continue
            temp2.append(i)
        team2.append(temp2)
    else:
        for i in range(now, N):
            make_team(k+1, i+1, temp+[i])


def balance(t1, t2):
    global result
    tmp1 = tmp2 = 0
    for i in t1:
        for j in t1:
            if i == j: continue
            tmp1 += arr[i][j]

    for i in t2:
        for j in t2:
            if i == j: continue
            tmp2 += arr[i][j]

    result = min(result, abs(tmp1-tmp2))


N = int(input())
team1 = []
team2 = []
result = 999999
arr = [list(map(int, input().split())) for _ in range(N)]
make_team(0, 0, [])
for k in range(len(team1)):
    balance(team1[k], team2[k])

print(result)
