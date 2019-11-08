test_num = int(input())
max_count = 0
max_result = ''
for num in range(test_num // 2, (test_num * 3 // 4) + 2):
    count = 2
    start = test_num
    end = num
    result = str(test_num) + ' ' + str(num)
    while True:
        if start - end < 0:
            break
        else:
            anchor = start - end
            start = end
            end = anchor
            count += 1
            result += ' ' + str(anchor)
    if max_count < count:
        max_count = count
        max_result = result

print(max_count)
print(max_result)
