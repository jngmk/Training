import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for a in range(N//2+1 if N % 2 else N//2):
        for b in range(1, N-1):
            for d1 in range(1, b+1):
                for d2 in range(1, N-b):
                    tmp = [arr[a][b]]
                    visited = [(a, b)]
                    aa, bb = a+d1+d2, b-d1+d2
                    if not (aa < N and 0 <= bb < N): continue
                    print(a, b, aa, bb)
                    for va, vb in [[aa, bb], [a+d1, b-d1], [aa-d1, bb+d1], [a+d2, b+d2], [aa-d2, bb-d2]]:
                        if (va, vb) in visited: continue
                        if arr[va][vb] in tmp: continue
                        tmp.append(arr[va][vb])
                        visited.append((va, vb))
                        print(tmp)
                    result = max(result, len(tmp))

    print('#{} {}'.format(tc, result))
    break