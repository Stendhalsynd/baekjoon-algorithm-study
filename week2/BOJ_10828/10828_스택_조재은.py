import sys

N = int(sys.stdin.readline()) # 명령의 수 N
stack = []

for i in range(N):
    command = sys.stdin.readline().split() # 둘째 줄부터 N개의 줄에는 명령이 하나씩

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif command[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])

