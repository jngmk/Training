# 2050. 알파벳을 숫자로 변환
# 131ms, 78

data_list = list(input())
for i in data_list:
    print(ord(i) - 64, end=' ')
