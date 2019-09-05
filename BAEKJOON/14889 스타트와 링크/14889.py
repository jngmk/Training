# 미결
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]


def calc(perm_list):
    sum_syn = 0
    for item in perm_list:
        print(1111, perm_list)
        print(item)
        sum_syn += array[item[0]][item[1]]
        sum_syn += array[item[1]][item[0]]
        print('sum_syn', sum_syn)

    return sum_syn


team_list = []
check = []
result = []
is_visited = [0] * N
is_visited_p = [0] * (N//2)
count = 0
nn = 0
min_syn = 100 * N


def comb(cnt, now):
    global result, check, min_syn, perm_sum, is_visited_p
    if result in check:
        print('check')
        return min_syn

    elif cnt == N//2:
        print('res, check', result, check)

        res2 = []
        for c in range(N):
            if c not in result:
                res2.append(c)
        check.append(result)
        check.append(res2)
        print(res2)
        perm_sum = 0
        now1 = 0
        is_visited_p = [0] * (N // 2)
        perm(count, now1, result)
        syn1 = perm_sum

        perm_sum = 0
        now1 = 0
        is_visited_p = [0] * (N // 2)
        perm(count, now1, res2)
        syn2 = perm_sum

        print(1, 2, syn1, syn2)
        syn = abs(syn1 - syn2)
        if min_syn > syn:
            min_syn = syn
        print(syn, min_syn)

    else:
        for i in range(now, N):
            print(result)
            if is_visited[i]:
                continue
            is_visited[i] = 1
            result.append(i)
            # print(1, result)
            comb(cnt+1, now+1)
            is_visited[i] = 0
            result = result[:-1]
            # print('-r', result)


def perm(cnt, now, team):
    global perm_sum, team_list
    if cnt == 2:
        print('cnt2, team_list', team_list)
        perm_sum += calc([team_list])
        print(perm_sum)
        # 하나씩 계산 함수로 보내기 때문에 계산 함수 값 다 더해서 리턴

    else:
        for i in range(now, len(team)):
            if is_visited_p[i]:
                continue
            print('n,l =', now, len(team), is_visited_p)
            is_visited_p[i] = 1
            team_list.append(team[i])
            perm(cnt+1, now+1, team)
            is_visited_p[i] = 0
            team_list = team_list[:-1]
            print('r', team_list)


comb(count, nn)
print(min_syn)
