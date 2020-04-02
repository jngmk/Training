def solution(n, build_frame):
    frames = dict()
    answer = []

    for build in build_frame:
        x, y, a, b = build  # 0: 기둥, 1: 보, 0: 삭제, 1: 설치
        if b == 1:
            frames.update({(x, y, a): 1})
            if check(frames.keys()):
                continue
            frames.pop((x, y, a))
        else:
            frames.pop((x, y, a))
            if check(frames.keys()):
                continue
            frames.update({(x, y, a): 1})
    for x, y, a in sorted((frames.keys())):
        answer.append([x, y, a])
    return answer


def check(frames):
    for x, y, a in frames:
        if a == 0:
            if not (y == 0 or (x, y, 1) in frames or (x-1, y, 1) in frames or (x, y-1, 0) in frames):
                return False
        else:
            if not ((x, y-1, 0) in frames or (x+1, y-1, 0) in frames or ((x-1, y, 1) in frames and (x+1, y, 1) in frames)):
                return False
    return True
