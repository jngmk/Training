import sys
input = sys.stdin.readline
from heapq import heapify, heappop

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
seats, people = [], []
s, p = 0, 0
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'X':
            p += 1
            people.append((r, c))
        elif arr[r][c] == 'L':
            s += 1
            seats.append((r, c))

min_seat_distance = [float('inf')] * s
competitors = [0] * s
decided_people = [0] * p
h = []
for s_idx in range(s):
    for p_idx in range(p):
        d = ((seats[s_idx][0] - people[p_idx][0]) ** 2) + ((seats[s_idx][1] - people[p_idx][1]) ** 2)
        h.append([d, s_idx, p_idx])
heapify(h)
while h:
    if p == 0: break
    d, ss, pp = heappop(h)
    if min_seat_distance[ss] < d: continue
    if decided_people[pp]: continue
    min_seat_distance[ss] = d
    competitors[ss] += 1
    decided_people[pp] = 1
    p -= 1

result = 0
for c in competitors:
    if c >= 2: result += 1
print(result)
