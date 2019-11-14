import sys
sys.stdin = open('input.txt')


def convert(arr):
    global convert_arr
    for i in range(N-1, -1, -N//4):
        idx = i
        tmp_num = 0
        for j in range(N//4):
            tmp_num += hex_num[arr[idx-j]] * (16 ** j)
        if tmp_num not in convert_arr:
            convert_arr.append(tmp_num)


hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    num_arr = list(input())
    convert_arr = []
    convert(num_arr)
    for _ in range(N//4):
        num_arr.append(num_arr.pop(0))
        convert(num_arr)
    convert_arr.sort(reverse=True)
    # print(convert_arr)
    print('#{} {}'.format(tc, convert_arr[K-1]))
    # break
