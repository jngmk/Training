# 부분집합 사용
D = int(input())
consult = [[0, 1, 0]]
max_pay = 0
check = [0] * (D+1)


def schedule(d):
    global max_pay
    if d > D:
        pay_sum = 0
        for c in range(D+1):
            if check[c]:
                pay_sum += consult[c][2]
                if max_pay < pay_sum:
                    max_pay = pay_sum
    else:
        schedule(d+1)
        if consult[d][1] <= D+1:
            check[consult[d][0]] = 1
        schedule(consult[d][1])
        if consult[d][1] <= D+1:
            check[consult[d][0]] = 0


for dd in range(1, D+1):
    term, pay = map(int, input().split())
    consult.append([dd, dd+term, pay])

schedule(0)
print(max_pay)
