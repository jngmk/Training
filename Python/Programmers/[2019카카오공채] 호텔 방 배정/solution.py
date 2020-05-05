visited = []


def solution(k, room_number):
    answer = []
    for room in room_number:
        # print('room', room)
        next_room = find_room(room)
        if next_room:
            answer.append(next_room)
        else:
            answer.append(room)
            idx = find_room(room)
            visited[idx:idx] = [[room, room]]
            sort_vis()

        flag = False
        while not flag:
            flag = combine_vis()
        # print(visited)
    return answer


def find_idx(room):
    global visited
    for i in range(len(visited)-1):
        if visited[i][1] < room < visited[i+1][0]:
            return i


def find_room(room):
    global visited
    for vis in visited:
        if vis[0] <= room <= vis[1]:
            vis[1] += 1
            return vis[1]
    return 0


def sort_vis():
    global visited
    visited.sort(key=lambda x: x[0])


def combine_vis():
    global visited
    for i in range(len(visited)-1):
        if visited[i][1] + 1 == visited[i+1][0]:
            visited[i][1] = visited[i+1][1]
            visited.pop(i+1)
            return False
    return True


dataset = [
    [10, [1,3,4,1,3,1]],
]

for k, room_number in dataset:
    print(solution(k, room_number))