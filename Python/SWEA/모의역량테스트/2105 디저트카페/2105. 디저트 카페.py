import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1 :
        return True
    return False
    
def solve(i, j, mode, result):
    global start
    global max_result
    print(result, "x :",i,"y :",j, 'mode:',mode)
    if data[i][j] in result:
        if [i, j] == start:
            if max_result < len(result):
                max_result = len(result)
        return
    # result.append(data[i][j])
    x = i
    y = j
    Testx = x + dx[mode]
    Testy = y + dy[mode]
    print(Testx, Testy)

    if isWall(Testx,Testy):
        print('ing')
        return
    solve(Testx, Testy, mode, result+[data[i][j]])
    solve(Testx, Testy, mode+1, result+[data[i][j]])


for test_case in range(1, TC+1):

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_result = -1
    for i in range(N-2):
        for j in range(N):
            if j == 0 or j == N - 1:
                continue
            start = [i, j]
            print("시작: ",start)
            solve(i, j, 0, [])
            print(max_result)
    break