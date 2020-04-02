def solution(key, lock):
    N = len(lock)
    v, vac = vacant(lock)

    if not vac: return True
    vac = vac[0]

    find = False
    for key in rotate(key):
        for i in range(len(key)):
            cnt = 0
            rr, cc = vac[0]-key[i][0], vac[1]-key[i][1]
            for j in range(i, len(key)):
                r, c = key[j]
                r, c = r+rr, c+cc
                if not (0 <= r < N and 0 <= c < N): continue
                if lock[r][c] == 1: break
                cnt += 1
            if cnt == v:
                find = True
                break
        if find: break
    if find: return True
    return False


def vacant(lock):
    N = len(lock)
    vac = []
    v = 0
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 0:
                vac.append((r, c))
                v += 1
    return v, vac


def rotate(key):
    M = len(key)
    key1 = [(r, c) for r in range(M) for c in range(M) if key[r][c] == 1]
    key2 = [(M-r-1, c) for c, r in key1]
    key3 = [(r, M-c-1) for c, r in key1]
    key4 = [(M-r-1, M-c-1) for r, c in key1]

    key1 = quick_sort(key1)
    key2 = quick_sort(key2)
    key3 = quick_sort(key3)
    key4 = quick_sort(key4)

    return key1, key2, key3, key4


def quick_sort(arr):
    if not arr: return []
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [pivot], []

    for pos in arr:
        if pos[0] < pivot[0]:
            lesser.append(pos)
        elif pos[0] > pivot[0]:
            greater.append(pos)
        else:
            if pos[1] < pivot[1]:
                lesser.append(pos)
            elif pos[1] > pivot[1]:
                greater.append(pos)

    return quick_sort(lesser) + equal + quick_sort(greater)
