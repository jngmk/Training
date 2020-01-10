def search(lo, hi, n):
    if lo == hi:
        return lo
    elif lo + 1 == hi:
        return lo if lis[lo] >= n else hi

    mid = (lo + hi) // 2
    if lis[mid] == n:
        return mid
    elif lis[mid] < n:
        return search(mid+1, hi, n)
    else:
        return search(lo, mid, n)


N = int(input())
A = list(map(int, input().split()))
INF = float('inf')
lis = [INF] * (N+1)
lis[0] = -INF
lis[1] = A[0]
trace = [-1]
max_length = 0

for a in A:
    if lis[max_length] < a:
        trace.append(max_length)
        max_length += 1
        lis[max_length] = a
    else:
        nxt = search(0, max_length, a)
        trace.append(nxt-1)
        lis[nxt] = a

print(max_length)
# print(trace)
ans = []
trace_idx = len(trace)-1
while max_length-1 != -1:
    if trace[trace_idx] == max_length-1:
        ans.append(A[trace_idx-1])
        max_length -= 1
        # print(trace_idx, A[trace_idx-1])
    trace_idx -= 1

print(' '.join(reversed(list(map(str, ans)))))
