"""
Input: N(사진틀의 개수) / M(전체 학생의 총 추천 횟수) / num(추천받은 학생을 나타내는 번호)
Output: 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력
Constraints: 1 <= N <= 20 / M <= 1,000 / 1 <= num <= 100

문제 정리:
학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정
추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙
1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
2. 어떤 학생이 특정 학생을 추천하면, 추천 받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제, 그 자리에 새롭게 추천받은 학생의 사진을 게시
이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된지 가장 오래된 사진 삭제
4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
5. 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

풀이:
딕셔너리 형태
Key: 후보자 번호
Value: [추천수, 들어온 순서]

1. 사진 틀에 후보자 사진이 존재하는 경우: 추천수 + 1
2. 사진 틀에 후보자 사진이 존재하지 않는 경우
    2-1. 비어있는 사진 틀이 존재하는 경우
        후보자 번호 num[i]인 학생의 사진 추가, 추천 횟수 1번, i번째 추천을 받았다는 정보를 photo 딕셔너리에 추가
    2-2. 비어있는 사진 틀이 없는 경우
        photo 딕셔너리의 항목을 추천 횟수 기준으로 먼저 정렬
        현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우의 상황을 위해서 들어온 순서를 기준으로 정렬한 리스트를 반환
        -> 이 결과 del_list의 첫번째에 있는 요소 = 추천 횟수가 가장 적고, 게시된지 가장 오랜된 사진
        -> 해당 요소의 key를 반환하여 photo 딕셔너리에서 제거
        -> 새롭게 추천된 사람을 photo 딕셔너리에 추가

시간복잡도: 루프 M번 반복: O(M), sorted 함수: O(NlogN) -> O(M * NlogN) (N: 사진 틀의 개수) -> M, N 모두 선형적으로 증가한다고 가정했을 때, O(N^2 * logN)
공간복잡도: photo 딕셔너리에 최대 N명의 후보에 대한 정보가 저장 -> O(N)
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split(" ")))

photo = dict()
for i in range(M) :
    # 사진틀에 후보자 사진이 존재하는 경우
    if num[i] in photo : 
        # 추천수 + 1
        photo[num[i]][0] += 1
    # 사진틀에 후보자 사진이 존재하지 않는 경우
    else : 
        # 비어있는 사진 틀이 있는 경우
        if len(photo) < N :
            # 후보자 번호 num[i]인 학생의 사진 추가, 추천 횟수 1번, i번째 추천이라는 의미
            photo[num[i]] = [1, i]
        # 비어있는 사진 틀이 없는 경우
        else :
            # photo 딕셔너리의 항목을 추천 횟수를 기준으로 먼저 정렬, 추천 횟수가 동일한 경우 들어온 순서를 기준으로 정렬한 리스트를 반환
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]))
            # photo.items(): 딕셔너리의 키-값 쌍을 (키, 값) 형태의 튜플로 반환한다.
            # key = lambda x: (x[1][0], x[1][1]): sorted 함수에 전달되는 정렬 키
            # x = photo.items()에서 가져온 각 튜플
            # x[1] = 튜플의 두번재 원소 -> (추천 횟수, 들어온 순서)로 이루어진 튜플
            # (x[1][0], x[1][1]) = (추천 횟수, 들어온 순서)
            
            # del_key = 추천 횟수가 가장 적고, 게시된지 가장 오래된 사진의 key
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1: ] :
    answer += " " + str(i)
print(answer)