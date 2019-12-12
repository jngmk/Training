def calc():
    global top, stack
    for c in commands:
        if len(c) > 3:  # NUM
            top += 1
            stack[top] = int(c[4:])
        elif c == 'POP':
            top -= 1
            if top == -2: return 'ERROR'
        elif c == 'INV':
            stack[top] = -stack[top]
        elif c == 'DUP':
            top += 1
            stack[top] = stack[top-1]
        # 계산을 할 수 없는 경우 에러
        elif top <= 0: return 'ERROR'
        elif c == 'SWP':
            stack[top], stack[top-1] = stack[top-1], stack[top]
        elif c == 'ADD':
            top -= 1
            stack[top] = stack[top] + stack[top+1]
        elif c == 'SUB':
            top -= 1
            stack[top] = stack[top] - stack[top+1]
        elif c == 'MUL':
            top -= 1
            stack[top] = stack[top] * stack[top+1]
        elif c == 'DIV':
            top -= 1
            if stack[top+1] == 0: return 'ERROR'
            sign = 1 if stack[top] * stack[top+1] > 0 else -1
            stack[top] = (abs(stack[top]) // abs(stack[top+1])) * sign
        elif c == 'MOD':
            top -= 1
            if stack[top+1] == 0: return 'ERROR'
            sign = 1 if stack[top] > 0 else -1
            stack[top] = (abs(stack[top]) % abs(stack[top+1])) * sign
        if abs(stack[top]) > 1e9: return 'ERROR'
    return stack[top] if top == 0 else 'ERROR'


is_quit = False
start = False
stack = [0] * 10000
top = -1

while True:
    commands = []
    while True:
        command = input()
        if command == 'END': break
        if command == 'QUIT': is_quit = True; break
        commands.append(command)
    if not is_quit:
        if start: print()
    if is_quit: break

    start = True
    N = int(input())
    while True:
        n = input()
        if n == '': break
        top = 0
        stack[top] = int(n)
        print(calc())
