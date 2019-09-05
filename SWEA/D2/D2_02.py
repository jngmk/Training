# 1284. 수도 요금 경쟁
# 122ms, 366
T = int(input())

def price_b(Q, R, S, W):
    if W <= R:
        price = Q
    else:
        price = Q + (S * (W - R))
    return price


for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    price_a = P * W
        
    if price_a < price_b(Q, R, S, W):
        print(f'#{i + 1} {price_a}')
    else:
        print(f'#{i + 1} {price_b(Q, R, S, W)}')
