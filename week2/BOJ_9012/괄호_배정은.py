import sys

T = int(sys.stdin.readline())

for _ in range(T):
    VPS = list(sys.stdin.readline().rstrip())
    stack = [VPS[0]]  # 스택
    for i in range(1, len(VPS)):
        if len(stack) > 0 and stack[-1] == '(' and VPS[i] == ")":
            stack.pop()
        else:
            stack.append(VPS[i])
    print("YES" if len(stack) == 0 else "NO")

