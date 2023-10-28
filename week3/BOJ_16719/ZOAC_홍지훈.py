# 구현, 문자열, 재귀
import sys

s = sys.stdin.readline().rstrip()
c = [False] * len(s)

def foo(l, r):

    if l == r: return

    mini = min(s[l:r])
    idx = s[l:r].index(mini) + l

    c[idx] = True

    for i in range(len(s)):
        if c[i]:
            print(s[i], end='')
    print()
    foo(idx + 1, r)
    foo(l, idx)

foo(0, len(s))