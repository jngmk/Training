def solution(lines):
    max_ans = 0
    times = []
    for line in lines:
        date, time, elapsed = line.split()
        time = list(map(float, time.split(':')))
        end_time = time[0] * 60 * 60 + time[1] * 60 + time[2]
        end_time = round(end_time, 3)
        start_time = end_time - float(elapsed[:-1]) + 0.001
        start_time = round(start_time, 3)
        times.append([start_time, end_time])

    for time in times:
        for t in time:
            for dt in -1, 1:
                start, end = list(sorted([t, t+dt]))
                ans = 0
                for s, e in times:
                    if not (e < start or end <= s): ans += 1
                max_ans = max(max_ans, ans)
    return max_ans
