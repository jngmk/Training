# 2029. 몫과 나머지 출력하기
# 125ms, 113

T = int(input())
for i in range(T):
    a, b = map(int, input().split(' '))
    print(f'#{i+1} {a // b} {a % b}')