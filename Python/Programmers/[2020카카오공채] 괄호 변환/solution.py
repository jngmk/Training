def solution(p):
    if is_correct(p): return p

    answer = solve(p)
    return answer


def solve(parenthesis):
    if parenthesis == '': return ''

    answer = ''
    slice_num = is_balance(parenthesis)
    u, v = parenthesis[:slice_num], parenthesis[slice_num:]
    if is_correct(u):
        answer += u
        answer += solve(v)
        return answer
    else:
        answer += '('
        answer += solve(v)
        answer += ')'

        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer


def is_correct(parenthesis):
    stack = []
    for p in parenthesis:
        if p == '(':
            stack.append('p')
        else:
            if not stack: return False
            stack.pop()

    if stack: return False
    return True


def is_balance(parenthesis):
    left, right = 0, 0

    length = len(parenthesis)
    for i in range(length):
        if parenthesis[i] == '(':
            left += 1
        else:
            right += 1

        if left == right: return i + 1

    return length
