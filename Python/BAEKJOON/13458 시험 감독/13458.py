N = int(input())
classes = list(map(int, input().split()))
f, s = map(int, input().split())
result = 0

for num in classes:
    cnt = 1
    num -= f
    if num > 0:
        if num % s == 0:
            cnt += num // s
        else:
            cnt += num // s
            cnt += 1

    result += cnt

print(result)
