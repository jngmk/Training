# 4, 14, 15, 16 틀림

def solution(n, t, m, timetable):
    bus_schedule = []
    hh, mm = 9, 0
    cnt = 0
    for _ in range(n):
        hh, mm = calc_clock(hh, mm, t * cnt)
        bus_schedule.append([hh, mm])
        cnt += 1
    print(bus_schedule)

    bus_idx = 0
    person_idx = 0
    group_list = []
    group = []
    timetable = list(sorted(map(preprocess, timetable)))
    if len(timetable) == 0:
        hh, mm = bus_schedule[-1]
        return '%02d:%02d'%(hh, mm)
    print(timetable)
    while True:
        if person_idx >= len(timetable): break
        if bus_idx >= n: break

        hh, mm = timetable[person_idx]
        nh, nm = bus_schedule[bus_idx]
        if ride(nh, nm, hh, mm):
            group.append([hh, mm])
            person_idx += 1
        else:
            group_list.append(group)
            bus_idx += 1
            group = []
        if len(group) == m:
            group_list.append(group)
            bus_idx += 1
            group = []

    if len(group_list) < n and len(group) > 0:
        group_list.append(group)
    print('group_list', group_list)

    hh, mm = get_answer(bus_schedule, group_list, m)
    hh, mm = calc_clock(hh, mm, 0)

    return '%02d:%02d'%(hh, mm)


def calc_clock(hh, mm, plus):
    mm += plus
    if mm >= 60:
        hh += 1
        mm %= 60

    if mm < 0:
        hh -= 1
        mm += 60
    return hh, mm


def preprocess(x):
    return list(map(int, x.split(':')))


def ride(ah, am, bh, bm):  # bus, person
    if bh < ah:
        return True
    if bh == ah and bm <= am:
        return True
    return False


def get_answer(bus_schedule, group_list, m):
    if len(group_list[-1]) < m:
        return bus_schedule[-1]
    return group_list[-1][-1][0], group_list[-1][-1][1]-1



dataset = [
    # [1, 1, 5, ['08:00', '08:01', '08:02', '08:03']],
    # [2, 10, 2, ['09:10', '09:09', '08:00']],
    [1, 1, 1, []],
    # [1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']],
    # [1, 1, 1, ['23:59']],
    # [10, 60, 45, ['23:59','23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']],
]

for n, t, m, timetable in dataset:
    print(solution(n, t, m, timetable))
    # break