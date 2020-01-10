# 시간 초과
n = int(input())
a = [0] + list(map(int, input().split()))
DP = [0] * (n + 1)
v = [-1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i, 1):
        # 자신(i)보다 값(a)은 작으면서 길이(DP)는 크다면
        if a[i] > a[i - j] and DP[i] < DP[i - j]:
            DP[i] = DP[i - j]
            v[i] = i - j  # 역 추적 하기 위한 인덱스를 배열에 저장
    DP[i] += 1

print(max(DP))

# 역추적 하기 위해 추가된 부분
ans = []
max_idx = DP.index(max(DP))
while max_idx != -1:
    ans.append(a[max_idx])
    max_idx = v[max_idx]
ans.reverse()

print(' '.join(map(str, ans)))