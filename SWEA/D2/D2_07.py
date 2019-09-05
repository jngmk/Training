# 1945. 간단한 소인수분해
# 121ms, 620

T = int(input())

def factoriztion(n):
    a, b, c, d, e = 0, 0, 0, 0, 0
    
    while True:
        a += 1
        if n % (2 ** a) != 0:
            break


    while True:
        b += 1
        if n % (3 ** b) != 0:
            break


    while True:
        c += 1
        if n % (5 ** c) != 0:
            break


    while True:
        d += 1
        if n % (7 ** d) != 0:
            break


    while True:
        e += 1
        if n % (11 ** e) != 0:
            break

    return f'{a - 1} {b - 1} {c - 1} {d - 1} {e - 1}'


for i in range(T):
    n = int(input())
    print(f'#{i + 1} {factoriztion(n)}')
