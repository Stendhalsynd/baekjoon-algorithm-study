import sys

T = int(sys.stdin.readline()) #  입력 데이터의 수

for _ in range(T):
    line = input()
    stack = []

    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')


