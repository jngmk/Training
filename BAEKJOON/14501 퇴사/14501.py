# DP 사용
D = int(input())
consult = [[0, 1, 0]]  # day, end_day+1, pay
max_pay = 0
check = [0] * (D+1)
result = [0] * (D+1)

for dd in range(1, D+1):
    term, pay = map(int, input().split())
    consult.append([dd, dd+term, pay])

for v in range(1, D+1):
    pay = []
    if consult[v][1] <= D+1:
        for a in range(v):
            if consult[a][1] <= D+1 and v - consult[a][1] >= 0:
                pay.append(result[a])
        result[v] = max(pay)+consult[v][2]

print(max(result))
