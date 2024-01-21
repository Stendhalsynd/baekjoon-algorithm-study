from collections import deque
import sys

input = sys.stdin.readline

# 1. 크기가 가장 큰 블록을 찾는다.
def find_block(i, j, block_num):
	q = deque()
	q.append((i, j))

	normals = [[i, j]]
	rainbows = []

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n:
				#무지개 블록을 만난 경우
				if block[nx][ny] == 0 and not visited[nx][ny]:
					q.append((nx, ny))
					rainbows.append([nx, ny])
					visited[nx][ny] = 1

				elif block[nx][ny] == block_num and not visited[nx][ny]:
					q.append((nx, ny))
					normals.append([nx, ny])
					visited[nx][ny] = 1

	for x, y in rainbows: # 무지개 블록들은 visited = False 처리
		visited[x][y] = 0

	# 블록 수, 무지개 블록 수, 그룹 내 불록들 위치 정보
	return [len(normals + rainbows), len(rainbows), normals + rainbows]
			
			
# 2. find_block에서 찾은 모든 블록을 제거한다.
def remove_block(group):
	global score

	score += group[0] ** 2

	for x, y in group[2]:
		block[x][y] = -2 # 제거된 블록은 -2로 표시

# 3. 중력이 작용한다.
def gravity():
	for i in range(n-2, -1, -1):
		for j in range(n):
			if block[i][j] != -1:
				pointer = i

				while pointer + 1 < n and block[pointer + 1][j] == -2:
					block[pointer + 1][j] = block[pointer][j]
					block[pointer][j] = -2
					pointer += 1

# 4. 90' 반 시계 방향으로 회전한다.
def rotate_block():
	global block
	
	tmp = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			tmp[n-j-1][i] = block[i][j]

	block = tmp


n, m = map(int, input().rstrip('\n').split())

block = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

score = 0

while True:
	visited = [[0] * n for _ in range(n)]
	groups = []
	
	for i in range(n):
		for j in range(n):
			if block[i][j] >= 1 and not visited[i][j]:
				visited[i][j] = 1
				group = find_block(i, j, block[i][j])

				if group[0] >= 2:
					groups.append(group)

	groups.sort(reverse = True)
	
	if not groups:
		break

	remove_block(groups[0])
	gravity()
	rotate_block()
	gravity()
	
print(score)