import sys

# 키보드 세팅
left_keyboard = [['q', 'w', 'e', 'r', 't'], ['a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v']]
right_keyboard = [[' ', ' ', ' ', ' ', ' ', 'y', 'u', 'i', 'o', 'p'], [' ', ' ', ' ', ' ', ' ', 'h', 'j', 'k', 'l'], [' ', ' ', ' ', ' ', 'b', 'n', 'm']] # 우측 손은 위치가 다르기때문에 공백을 넣음
left_keyboard_dict, right_keyboard_dict = dict(), dict()
for i in range(len(left_keyboard)):
    for j in range(len(left_keyboard[i])):
        left_keyboard_dict[left_keyboard[i][j]] = [i, j]

for i in range(len(right_keyboard)):
    for j in range(len(right_keyboard[i])):
        right_keyboard_dict[right_keyboard[i][j]] = [i, j]

S_l, S_R = map(str, sys.stdin.readline().split())
S = sys.stdin.readline().rstrip()

S_l_coord, S_R_coord = left_keyboard_dict[S_l], right_keyboard_dict[S_R]

ans = 0
for s in S:
    if left_keyboard_dict.get(s) is not None:
        s_coord = left_keyboard_dict[s]
        ans += (abs(S_l_coord[0] - s_coord[0]) + abs(S_l_coord[1] - s_coord[1])) + 1
        S_l_coord = s_coord
    else:
        s_coord = right_keyboard_dict[s]
        ans += (abs(S_R_coord[0] - s_coord[0]) + abs(S_R_coord[1] - s_coord[1])) + 1
        S_R_coord =s_coord

print(ans)