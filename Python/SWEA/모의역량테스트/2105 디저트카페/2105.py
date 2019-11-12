import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for a in range(N//2+1 if N % 2 else N//2):
        for b in range(1, N-1):
            tmp = [arr[a][b]]
            aa, bb = N-a-1, N-b-1
            print(a, b, aa, bb)
            if arr[aa][bb] in tmp: continue
            tmp.append(arr[aa][bb])
            for d in range(1, b+1):
                if arr[a+d][b-d] in tmp: continue
                tmp.append(arr[a+d][b-d])
                if arr[aa-d][bb+d] in tmp: continue
                tmp.append(arr[aa-d][bb+d])
            for d in range(1, N-b-1):
                if arr[a+d][b+d] in tmp: continue
                tmp.append(arr[a+d][b+d])
                if arr[aa-d][bb-d] in tmp: continue
                tmp.append(arr[aa-d][bb-d])
            result = max(result, len(tmp))

    print('#{} {}'.format(tc, result))
