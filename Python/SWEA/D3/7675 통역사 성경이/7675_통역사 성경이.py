# 7675. 통역사 성경이
# 190ms, 743
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    num_line = int(input())
    line_list = input()
    for q in ['.', '!', '?']:
        line_list = line_list.replace(q, '{0}/'.format(q))
    line_list = list(map(str, line_list.split('/')))

    check_num_list = list(map(str, list(range(10))))
    word_list = []
    result = ''
    for j in range(num_line):
        word_list = list(map(str, line_list[j].split()))
        word_cnt = 0
        for k in word_list:
            if k == k.capitalize():
                word_cnt += 1
                for l in k:
                    if l in check_num_list:
                        word_cnt -= 1
                        break

        result += str(word_cnt) + ' '

    print('#{0} {1}'.format(i+1, result))
