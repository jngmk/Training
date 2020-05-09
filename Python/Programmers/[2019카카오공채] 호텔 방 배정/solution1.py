import sys
sys.setrecursionlimit(1500)


def find_room(room, visited):
    if room not in visited:
        visited[room] = room + 1
        return room
    next_room = find_room(visited[room], visited)
    visited[room] = next_room + 1
    return next_room


def solution(k, room_number):
    answer = []
    visited = dict()
    for room in room_number:
        room_num = find_room(room, visited)
        answer.append(room_num)
    return answer


dataset = [
    [10, [1,3,4,1,3,1]],
]

for k, room_number in dataset:
    print(solution(k, room_number))