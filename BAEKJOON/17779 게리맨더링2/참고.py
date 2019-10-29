n = int(input())
grid = [[]] + [[0]+list(map(int,input().split())) for i in range(n)]
ans = 99**9


def divide(x, y, d1, d2):
    pop = [0]*5
    for r in range(1, n+1):
        for c in range(1, n+1):
            if x+y <= r+c <= x+y+2*d2 and y-x-2*d1 <= c-r <= y-x:
                pop[4]+= grid[r][c]
            elif 1<=r<x+d1 and 1<=c<=y: pop[0]+= grid[r][c]
            elif 1<=r<=x+d2 and y<c<=n: pop[1]+= grid[r][c]
            elif x+d1<=r<=n and 1<=c<y-d1+d2: pop[2]+= grid[r][c]
            else: pop[3]+= grid[r][c]
    return max(pop) - min(pop)


for x in range(1, n):
    for y in range(1, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if not (x+d1+d2<=n and 1<=y-d1 and y+d2<=n): continue
                ans = min(ans, divide(x, y, d1, d2))
print(ans)