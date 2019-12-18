N = int(input())
if N == 1: print(2); print('[+] [/]')
elif N == 2: print(1); print('[+]')
else:
    def converting(x):
        if x == 1: return '[+]'
        elif x == 2: return '[-]'
        elif x == 3: return '[*]'
        else: return '[/]'
    binary = []
    length = 1
    while True:
        if N == 1: binary.append(1); break
        if N == 2: binary.extend([0, 1]); length += 1; break
        if N % 2 == 1: binary.append(1)
        else: binary.append(0)
        N //= 2
        length += 1
    result = [1]
    cnt = 1
    possible = True
    for n in range(length-2, -1, -1):
        if cnt > 99: possible = False; print(-1); break
        if n != 0:
            if binary[n] == 1:
                result.extend([3, 1])
                cnt += 2
            else:
                result.append(3)
                cnt += 1
        else:
            if binary[n] == 1:
                result.extend([3, 1, 4])
                cnt += 3
    if possible:
        print(len(result))
        result = list(map(converting, result))
        print(' '.join(result))
