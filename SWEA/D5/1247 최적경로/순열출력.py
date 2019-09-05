def permutation(k):
    global temp
    global result_list

    if k == N:
        result_list.append(temp)

        return True
    else:
        for i in range(len(arr)):
            if visited[i]:
                continue
            visited[i] = 1
            temp.append(arr[i])
            permutation(k+1)
            visited[i] = 0
            temp = temp[:-1]


N = 2
arr = ['a', 'b', 'c']
visited = [0] * len(arr)

result_list = []
temp = []
permutation(0)
print(result_list)