from pprint import pprint
import sys
sys.stdin = open('input.txt')

da, db = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    life_arr = [[0] * (2*K+M) for _ in range(2*K+M)]
    status_arr = [[0] * (2*K+M) for _ in range(2*K+M)]  # 0 번식가능공간, 1 비활성, 2 활성, 3 죽음
    activate, tmp_activate, non_activate = {}, {}, {}
    for a in range(N):
        tmp = list(map(int, input().split()))
        for b in range(M):
            life_arr[a+K][b+K] = tmp[b]
            if tmp[b] > 0:
                non_activate[(a+K, b+K)] = tmp[b]  # 좌표, 생명력
                status_arr[a+K][b+K] = 1

    print('non', non_activate)
    print(activate)
    pprint(life_arr)
    print()
    pprint(status_arr)
    # K번 번식
    for _ in range(K):
        # 활성
        for a, b in list(activate.keys()):
            l = activate[(a, b)]
            l -= 1
            # 번식, 죽음
            if l == 0:
                activate.pop((a, b))
                status_arr[a][b] = 3
                for d in range(4):
                    va, vb = a + da[d], b + db[d]
                    # 동시번식
                    if status_arr[va][vb] == 1 and non_activate.get((va, vb)) == life_arr[va][vb] and \
                            life_arr[a][b] > life_arr[va][vb]:
                        non_activate[(va, vb)] = life_arr[a][b]
                        life_arr[va][vb] = life_arr[a][b]
                    elif status_arr[va][vb] == 0:
                        non_activate[(va, vb)] = life_arr[a][b]
                        life_arr[va][vb] = life_arr[a][b]
            else:
                activate[(a, b)] = l
        # 비활성
        for a, b in list(non_activate.keys()):
            l = non_activate[(a, b)]
            l -= 1
            # 활성전환
            if l == 0:
                non_activate.pop((a, b))
                activate[(a, b)] = life_arr[a][b]
                status_arr[a][b] = 2
            else:
                non_activate[(a, b)] = l

        # # 비활성 - 활성
        # for key, item in tmp_activate.items():
        #     activate[key] = item

        print('non', non_activate)
        print(activate)
        pprint(life_arr)
        print()
        pprint(status_arr)

    print('#{} {}'.format(tc, len(activate)+len(non_activate)))
    break