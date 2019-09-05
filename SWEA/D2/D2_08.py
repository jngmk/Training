# 1946. 간단한 압축 풀기
# 137 ms, 458

T = int(input())
for i in range(T):
    t = int(input())
    result = ''
    print(f'#{i + 1}')

    for j in range(t):
        Ci, Ki = input().split(' ')
        Ki = int(Ki)
        result += Ci * Ki
        
    for k in range(1, len(result) + 1):
        if k % 10 == 0:
            print(result[k - 10:k])

        if k == len(result):
            if k % 10 != 0:
                r = len(result) % 10
                print(result[len(result) - r:])
