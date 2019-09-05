# 1936.
# 133ms, 321

data_list = input().split(" ")
a = data_list[0]
b = data_list[1]

if a == '1' and b == '2':
    print("B")
elif a == '1' and b == '3':
    print("A")
elif a == '2' and b == '3':
    print("B")
elif a == '2' and b == '1':
    print("A")
elif a == '3' and b == '1':
    print("B")
elif a == '3' and b == '2':
    print("A")