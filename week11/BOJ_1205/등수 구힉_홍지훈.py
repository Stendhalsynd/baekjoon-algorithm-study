import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

'''
N: 리스트에 있는 점수의 개수
next_score: 태수의 새로운 점수
P: 랭킹 리스트에 올라 갈 수 있는 점수의 개수
'''
N, next_score, P = map(int,input().rstrip().split()) 

scores = list(map(int, input().rstrip().split()))
scores.reverse()

answer = len(scores) + 1 - bisect_right(scores, next_score)
count = len(scores) + 1 - bisect_left(scores, next_score)

[print(-1) if count > P else print(answer)]