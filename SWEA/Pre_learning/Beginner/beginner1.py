#problem7
Inch = float(input())
Cm = Inch*2.54
Output = "{0:0.2f} inch =>  {1:0.2f} cm".format(Inch, Cm)
print(Output)

#problem8
Kg = float(input())
Lb = Kg*2.2046
Output1 = "{0:0.2f} kg =>  {1:0.2f} lb".format(Kg, Lb)
print(Output1)

#problem9
섭씨 = float(input())
화씨 = 32+(섭씨/100*180)
Output2 = "{0:0.2f} ℃ =>  {1:0.2f} ℉".format(섭씨, 화씨)
print(Output2)

#problem10
화씨1 = float(input())
섭씨1 = (화씨1-32)/180*100
Output3 = "{0:0.2f} ℉ =>  {1:0.2f} ℃".format(화씨1, 섭씨1)
print(Output3)

#problem11
sum = (0.2*100)/(100+200)*100
Output4 = "혼합된 소금물의 농도: %0.2f%%" % sum
print(Output4)

#problem13
약수구하기 = int(input())
for i in range (1, 약수구하기+1, 1):
    if 약수구하기 % i == 0:
        print("%d(은)는 %d의 약수입니다." % (i, 약수구하기))

#problem14
약수구하기1 = int(input())
약수의합 = 0
for i in range (1, 약수구하기1+1, 1):
    if 약수구하기1 % i == 0:
        약수의합 = 약수의합 + 1
        print("%d(은)는 %d의 약수입니다." % (i, 약수구하기1))
    if 약수의합 == 2:
        print("{0}(은)는 {1}과 {2}로만 나눌 수 있는 소수입니다.".format(약수구하기1, 1, 약수구하기1))

#problem15
입력소문자 = str(input())
소문자들 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
for 소문자 in 소문자들:
    if 입력소문자 == 소문자들[소문자]:
        print("%s 는 소문자 입니다." % 입력소문자)

#problem16
man1 = str(input())
man2 = str(input())

if man1 == man2:
    print("Result : Draw")
elif man1 == "가위" and man2 == "바위":
    print("Result : Man2 Win!")
elif man1 == "가위" and man2 == "보":
    print("Result : Man1 Win!")
elif man1 == "바위" and man2 == "보":
    print("Result : Man2 Win!")
elif man1 == "바위" and man2 == "가위":
    print("Result : Man1 Win!")
elif man1 == "보" and man2 == "가위":
    print("Result : Man2 Win!")
elif man1 == "보" and man2 == "바위":
    print("Result : Man1 Win!")

#problem17
입력알파벳 = str(input())
대문자 = 입력알파벳.upper()
if 입력알파벳 == 대문자:
    변환알파벳 = 입력알파벳.lower()
else:
    변환알파벳 = 입력알파벳.upper()

입력아스키 = ord(입력알파벳)
변환아스키 = ord(변환알파벳)

print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(입력알파벳, 입력아스키, 변환알파벳, 변환아스키))

# 문자를 "아스키 코드 번호"로 변환하려면 ord() 함수를 사용합니다. 
# 출력 결과를 10진수 숫자가 아닌 "16진수 문자열"로 출력하려면 hex() 함수를 사용합니다. (▶▶ Python/파이썬] 10진수 숫자를 16진수(헥사;Hex)로 변환 출력 참고)

# 그 반대로, "아스키 코드 번호"를 "실제 문자"로 변환하려면 chr() 함수를 사용합니다.
# chr(0x5A) 이렇게 "16진수 숫자"를 넣을 수도 있습니다.

#problem18
조건합계 = "7"
for i in range (8, 201, 1):
    if i % 7 == 0:
        if i % 5 == 0:
            continue
        조건합계 = 조건합계 + "," + str(i)
print(조건합계)

#problem19
짝수합계 = "200"
for i in range (201, 301, 1):
    if (i // 100) % 2 == 0:
        if ((i // 10) % 10) % 2 == 0:
            if (i % 10) % 2 == 0:
                짝수합계 = 짝수합계 + "," + str(i)
print(짝수합계)

#problem21
점수 = [88, 30, 61, 55, 95]
k = 1
for i in 점수:
    if i >= 60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(k, i))
        k = k + 1
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(k, i))
        k = k + 1
    
#problem22
for i in range (1, 101, 1):
    print(i)

#problem23
for i in range (1, 101, 1):
    if i % 2 == 0:
        print(i, end=' ')

#problem24
홀수합계 = "1"
for i in range (2, 101, 1):
    if i % 2 == 1:
        홀수합계 = 홀수합계 + ", " + str(i)
print(홀수합계)

#problem25
삼의배수합계 = 0
for i in range (1, 100, 1):
    if i % 3 == 0:
        삼의배수합계 = 삼의배수합계 + i
print("1부터 100사이의 숫자 중 3의 배수의 총합: %d" % 삼의배수합계)

#problem26
A형, B형, AB형, O형 = 0, 0, 0, 0
혈액형 = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for i in range(0, len(혈액형)):
    if 혈액형[i] == 'A':
        A형 = A형 + 1
    elif 혈액형[i] == 'B':
        B형 = B형 + 1
    elif 혈액형[i] == 'AB':
        AB형 = AB형 + 1
    else:
        O형 = O형 + 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" %(A형, O형, B형, AB형))

# myList =  [1, 2, 3, 4, 1, 4, 1]
# print myList.count(1)
# 중괄호 안에 중괄호 어떻게 출력하는지?

#problem27
점수 = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0
sum = 0

while i < len(점수):
    if 점수[i] >= 80:
        sum += 점수.pop(i)
    else:
        i += 1
    
print(sum)

#problem28
i = 5
while i > 0:
    print("*" * i)
    i = i - 1

#problem29
i = 0
j = 4

while i < 4:
    print("{0}{1}".format(" " * i, "*" * (2 * j - 1)))
    i += 1
    j -= 1

#problem30
임의숫자 = str(input())
분할 = list(임의숫자)
리스트 = "0"
개수리스트 = "0"

for i in range(1, 10, 1):
    리스트 = 리스트 + " " + str(i)

for j in range(1, 10, 1):
    문자변환 = str(j)
    수세기 = 분할.count(문자변환)
    개수리스트 = 개수리스트 + " " + str(수세기)

print(리스트)
print(개수리스트)
    
#problem31
i = 1
while i <= 5:
    print("{0:>5}".format("*" * i))
    i = i + 1

#problem32
이진수 = int(input())
이진수변환 = "{0:b}".format(이진수)
print(이진수변환)

#problem34
입력단어 = str(input())
회문판단 = "입력하신 단어는 회문(Palindrome)입니다."

if list(입력단어) == list(reversed(입력단어)):
    print(입력단어)
    print(회문판단)

# https://dojang.io/mod/page/view.php?id=2331

#problem35
def 가위바위보(a, b, a_pick, b_pick):
    
    if a_pick == b_pick:
        return "비겼습니다!"
    elif a_pick == "가위" and b_pick == "바위":
        return "바위가 이겼습니다!"
    elif a_pick == "가위" and b_pick == "보":
        return "가위가 이겼습니다!"
    elif a_pick == "바위" and b_pick == "보":
        return "보가 이겼습니다!"
    elif a_pick == "바위" and b_pick == "가위":
        return "바위가 이겼습니다!"
    elif a_pick == "보" and b_pick == "가위":
        return "가위가 이겼습니다!"
    elif a_pick == "보" and b_pick == "바위":
        return "보가 이겼습니다!"

a = str(input())
b = str(input())
a_pick = str(input())
b_pick = str(input())

print(가위바위보(a, b, a_pick, b_pick))

#problem36
소수 = int(input())
약수의합 = 0
for i in range (1, 소수+1, 1):
    if 소수 % i == 0:
        약수의합 = 약수의합 + 1
if 약수의합 == 2:
        print("소수입니다.")
else:
        print("소수가 아닙니다.")

#problem37
def fibUpto(n):
    a, b = 1, 1
    i = 1
    while i <= n:
        if a == 1:
            수열 = "1, 1"
        else:
            수열 = 수열 + ", " + str(a)
        a, b = b, a+b
        i = i + 1
    print("[{0}]".format(수열))

입력 = int(input())
fibUpto(입력)

#problem38
리스트 = [1, 2, 3, 4, 3, 2, 1]
중복제거 = list(set(리스트))

print(리스트)
print(중복제거)

#problem39
리스트1 = [2, 4, 6, 8, 10]
print(리스트1)
if 5 in 리스트1:
    print("5 => True")
else:
    print("5 => False")
if 10 in 리스트1:
    print("10 => True")

#problem40
def 팩토리얼(n):
    곱 = 1
    i = 1
    while i <= n:
        곱 = 곱 * i
        i = i + 1
    print({0},format(곱))

입력값 = int(input())
팩토리얼(입력값)

#problem41
def 제곱구하기(a, b):
    print("square({0}) => {1}".format(a, a ** 2))
    print("square({0}) => {1}".format(b, b ** 2))

가, 나 = map(int, input().split(','))
제곱구하기(가, 나)

# https://dojang.io/mod/page/view.php?id=2286

#problem42
가, 나 = map(str, input().split(','))
리스트1 = list(가)
리스트2 = list(나)

if len(리스트1) > len(리스트2):
    print(가)
else:
    print(나)

#problem43
def countdown(n):
    if n <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        i = n
        while i > 0:
            print(i)
            i = i - 1

countdown(0)
countdown(10)

#problem45
name = input()
age = int(input())
year = 2019 + 100 - age
print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, year))

#problem46
문자열 = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")
num_A = 문자열.count("A")
num_B = 문자열.count("B")
num_C = 문자열.count("C")
num_D = 문자열.count("D")

num_list = [num_A, num_B, num_C, num_D]
multiply_list = [4, 3, 2, 1]
m_num_list = list(map(lambda x, y: x * y, num_list, multiply_list))

num_sum = 0
for i in m_num_list:
    num_sum = num_sum + i

print(num_sum)

#problem47
def calc_mul(*params):
    total = 1
    for i in params:
        total = total * i
    return total

try:
    ret_val = calc_mul(int(input()))
    print(ret_val)
except:
    print("에러발생")



#problem48
숫자입력 = int(input())
print("ASCII {0} => {1}".format(숫자입력 ,chr(숫자입력)))

#problem49
숫자리스트 = list(range(1,11))
필터리스트 = list(filter(lambda x: x % 2 == 0, 숫자리스트))
print(필터리스트)

#problem50
숫자리스트 = list(range(1,11))
맵리스트 = list(map(lambda x: x ** 2, 숫자리스트))
print(맵리스트)

#problem51
숫자리스트 = list(range(1,11))
필터리스트 = list(filter(lambda x: x % 2 == 0, 숫자리스트))
맵리스트 = list(map(lambda x: x ** 2, 필터리스트))
print(맵리스트)

#problem52
def 최대값(*나열):
    result = max(나열)
    print("max(3, 5, 4, 1, 8, 10, 2) => {0}".format(result))

최대값(3, 5, 4, 1, 8, 10, 2)

#problem53
data_list1 = list('abcdef')
data_list2 = list(range(0,6))
data_dict = dict(zip(data_list1, data_list2))

for i in data_dict:
    print("{0}: {1}".format(i, data_dict[i]))