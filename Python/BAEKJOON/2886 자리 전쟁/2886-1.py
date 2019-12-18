import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
people = []
s, p = 0, 0
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'X':
            p += 1
            people.append((r, c))
        elif arr[r][c] == 'L':
            s += 1
            arr[r][c] = s

min_seat_distance = [float('inf')] * s
competitors = [0] * s
decided_people = [0] * p
h = []
visited = dict()  # (r, c, p_idx): 1
for p_idx in range(p):
    h.append([0, -1, p_idx, people[p][0], people[p][1]])  # distance, s_idx, p_idx, pos
heapify(h)

while p > 0:
    d, s_idx, p_idx, r, c = heappop(h)
    for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0):
        nr, nc = r+dr, c+dc
        if not (0 <= nr < R and 0 <= nc < C): continue
        nd = ((people[p_idx][0]-nr) ** 2) + ((people[p_idx][1]-nc) ** 2)