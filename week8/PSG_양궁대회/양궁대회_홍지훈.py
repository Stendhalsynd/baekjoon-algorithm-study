from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    max_score = 0
    current_max_board = {}
    
    # 어피치 점수 초기화
    apeach = {10: 0, 9: 0, 8:0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    for idx, val in enumerate(info):
        score = 10 - idx
        apeach[score] = val
    
    for cases in combinations_with_replacement([10,9,8,7,6,5,4,3,2,1,0], n):
        # 라이언 점수 초기화
        board = {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
        
        # 각 경우에 대해 라이언이 과녁에 점수별로 몇개의 화살을 쏜 것인지 계산
        for val in cases:
            board[val] += 1
        
        lion_score_sum = 0
        apeach_score_sum = 0
        for i in range(10, -1, -1):
            if board[i] == apeach[i] + 1: # 라이언이 점수를 획득하는 경우
                lion_score_sum += i
            else: # 어피치가 점수를 획득하는 경우
                if apeach[i] != 0:
                    apeach_score_sum += i

        gap = lion_score_sum - apeach_score_sum # 라이언과 어피치의 점수 차이
        if gap > 0 and gap > max_score: # 점수 차이가 최대가 되는 경우 갱신
            max_score = gap
            current_max_board = board

        elif gap > 0 and gap == max_score: # 점수 차이가 동일할때 가장 낮은 점수를 더 많이 맞힌 경우를 구해 갱신
            board_smallest = 10
            current_smallest = 10
            
            for key, val in list(board.items()): # 이번 경우에서 가장 낮은 점수 계산
                if val != 0:
                    board_smallest = key
                    
            for key, val in list(current_max_board.items()): # 현재까지 가장 낮은 점수 계산
                if val != 0:
                    current_smallest = key
            if board_smallest < current_smallest: # 점수 차이가 동일할때 가장 낮은 점수가 갱신되는 경우
                current_max_board = board
            elif board_smallest == current_smallest:
                if board[board_smallest] > current_max_board[current_smallest]: # 가장 낮은 점수가 동일할때 해당 점수를 더 많이 맞춘 경우 갱신
                    current_max_board = board
    
    if not current_max_board:
        return [-1]
    answer = list(current_max_board.values())
    
    return answer