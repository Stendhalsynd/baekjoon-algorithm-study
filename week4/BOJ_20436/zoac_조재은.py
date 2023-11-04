from sys import stdin

# 입력 갑 읽기
l, r = map(str, stdin.readline().rstrip().split())  # 자음 시작첨, 모음 시작점
string = stdin.readline().rstrip()                  # 받을 문자열

# 키보드 레이아웃
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']   # 전체 자판
mo = 'iophjklbnm'                                   # 모음
x1, y1, x2, y2 = None, None, None, None
ans = 0

# 처음 손 위치의 좌표
for i in range(len(keyboard)):
    # 자음
    if l in keyboard[i]:
        x1, y1 = i, keyboard[i].index(l)
        print("x1, y1", x1, y1)
    # 모음
    if r in keyboard[i]:
        x2, y2 = i, keyboard[i].index(r)
        print("x2, y2", x2, y2)
# 문자열
for s in string:
    ans += 1
    # 모음 확인 (o)
    if s in mo:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i # 리스트 인덱스 번호
                ny = keyboard[i].index(s) # 해당 배열의 인덱스 번호
                ans += abs(x2-nx) + abs(y2-ny)
                x2, y2 = nx, ny
                break
    # 자음 확인 (z, a, c)
    else:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)
                ans += abs(x1-nx) + abs(y1-ny)
                x1, y1 = nx, ny
                break

print(ans)