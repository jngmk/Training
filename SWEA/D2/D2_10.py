# 1954. 달팽이 숫자
#

T = int(input())
for i in range(T):
    t = int(input())
    nn_list = []
    for j in range(t):
        n_list = []
        for k in range(t):
            n_list.append('a')
        nn_list.append(n_list)
        print(nn_list)