# 파이썬 프로그래밍 기초(2) 파이썬의 기본 응용
# 3차시
a = (90, 80)
b = (85, 75)
c = (90, 100)

data_tuple = (a, b, c)

for i, score in enumerate(data_tuple):
    total = 0
    for j in score:
        total = total + j
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1F}입니다.".format(i+1, total, total / len(score)))

# 4차시 / https://kyun2.tistory.com/83
data_list = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
data_list1 = [item for item in data_list if item not in 'aeiou']
for i in data_list1:
    print(i, end='')

# 5차시
dan = []
for i in range(2, 10):
    dan_detail = []
    for j in range(1, 10):
        result = i * j
        if result % 3 == 0:
            continue
        elif result % 7 == 0:
            continue
        else:
            dan_detail.append(result)
    dan.append(dan_detail)
print(dan)

# 6차시
data_list = []
sum = 0
for i in range(5):
    data_list.append(int(input()))
    sum = sum + data_list[i]
print('입력된 값 {0}의 평균은 {1}입니다.'.format(data_list, sum/len(data_list)))

# 7차시
n = int(input())
data_list = range(1,n+1)
data_list1 = [x for x in data_list if n % x == 0]
print(data_list1)

# 8차시
n = int(input())
data_list = range(1,n+1)
data_list1 = [x for x in data_list if n % x == 0]
print(data_list1)

# 9차시
data_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
data_list1 = [x for x in data_list if x % 2 == 0]
print(data_list1)

# 10차시(미해결)
n = 10


# 11차시
result = [x ** 2 for x in range(1, 21) if x % 3 != 0 or x % 5 != 0]
print(result)

# 12차시
num_list = list(map(int, str(input())))
sum = 0
for i in num_list:
    sum = sum + i
print(sum)

# 13차시(미해결)
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'), ('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

result = [y for x in dicbase for y in inputWord if y in range(x[0], x[-1])]
print(result)

# 14차시
num_tuple = tuple(map(int, input().split(',')))
num_list = []
for num in num_tuple:
    num_list.append(num)

print(num_list)
print(num_tuple)