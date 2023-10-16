import sys

N = int(sys.stdin.readline()) # 명령의 수
stack = []
for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command[0] == "top":
        print(stack[-1] if len(stack) > 0 else -1)