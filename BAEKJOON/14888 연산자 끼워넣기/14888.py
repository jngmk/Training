N = int(input())
num_arr = list(map(int, input().split()))
temp1 = list(map(int, input().split()))
temp2 = ['+', '-', '*', '//']
operator = []
result = []
max_num = -1000000000
min_num = 1000000000
is_visited = [0] * (N-1)
for n in range(4):
    operator += [temp2[n]] * temp1[n]


def perm(k, temp):
    global result
    if k == N-1:
        result.append(temp)
    else:
        for i in range(N-1):
            if is_visited[i]:
                continue
            is_visited[i] = 1
            perm(k+1, temp + [operator[i]])
            is_visited[i] = 0


def calc(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    else:
        if n1 < 0:
            n1 = -n1
            return -(n1 // n2)
        else:
            return n1 // n2


perm(0, [])
for op in result:
    base = num_arr[0]
    for i in range(1, N):
        base = calc(base, num_arr[i], op[i-1])
    if max_num < base:
        max_num = base
        res1 = op
    if min_num > base:
        min_num = base
        res2 = op

print(max_num)
print(min_num)
