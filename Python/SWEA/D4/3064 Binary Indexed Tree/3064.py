for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []
    # 배열 만들기
    size, n = 0, 0
    while True:
        if 2 ** n >= N:
            size = 2 ** n
            break
        n += 1
    arr = [0] * size * 2
    arr[size:size+N] = nums
    for i in range(size*2-1, 1, -1):
        arr[i//2] += arr[i]
    # 명령 실행
    for _ in range(M):
        c, n1, n2 = map(int, input().split())
        if c == 1:
            idx = size+n1-1
            while True:
                if idx == 0: break
                arr[idx] += n2
                idx //= 2
        elif c == 2:
            s, e, total = size+n1-1, size+n2-1, 0
            while s < e:
                # 시작하는 값이 홀수일 때
                if s % 2 == 1:
                    total += arr[s]
                    s += 1
                # 끝나는 값이 짝수일 때
                if e % 2 == 0:
                    total += arr[e]
                    e -= 1
                s //= 2
                e //= 2
            if s == e: total += arr[s]
            result.append(str(total))
    print('#{} {}'.format(tc, ' '.join(result)))
