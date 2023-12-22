graph = [list(map(int, input().split())) for _ in range(19)]
moves = [(0, 1), (1, 0), (1, 1), (-1, 1)] # 오른쪽, 아래, 대각선 오른쪽 아래, 대각선 오른쪽 위 (가장 왼쪽에 있는 바둑알을 추출해내야하기 때문)

def find():
    found = False
    for i in range(19):
        for j in range(19):
            # 바둑알이 0이 아니면
            if graph[i][j] != 0:
                target = graph[i][j]  # 바둑알의 넘버를 타겟으로 잡는다.
                
                for move in moves:
                    count = 1

                    # 다음 바둑알들의 위치
                    newI = i + move[0]
                    newJ = j + move[1]

                    while 0 <= newI < 19 and 0 <= newJ < 19 and graph[newI][newJ] == target:
                        count += 1

                        # 육목 체크
                        if count == 5:
                            # 맨 앞의 바둑알 앞에 바둑알이 놓였을 경우 -> 육목
                            if 0 <= i - move[0] < 19 and 0 <= j - move[1] < 19 and graph[i - move[0]][j - move[1]] == target:
                                break
                            # 맨 뒤의 바둑알 뒤에 바둑알이 놓였을 경우 -> 육목
                            if 0 <= newI + move[0] < 19 and 0 <= newJ + move[1] < 19 and graph[newI + move[0]][newJ + move[1]] == target:
                                break
                            print(target)
                            print(i + 1, j + 1)
                            found = True
                            return
                        newI += move[0]
                        newJ += move[1]
    if not found:
        print(0)
        return
find()
