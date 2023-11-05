# 구현, 그리디 알고리즘, 문자열

import sys
input = sys.stdin.readline

str = input().rstrip()

duck = 'quack'
ducks = {}

def count(str, duck, ducks):
    for char in str:
      # 오리 울음이 시작하는 경우, 새로운 오리를 추가 ( ducks[idx] = 1 ) 하거나 기존 오리의 울음이 끝나고 새로운 울음이 시작하는 경우다.
      if char == 'q':
        hasFullValue = False
        for idx, val in enumerate(ducks.values()):
          if val == 5: # char 이 q 인데 기존 오리중 울음을 완료한 오리가 있다. 그 오리는 다시 울음을 시작한다.
            ducks[idx] = 1
            hasFullValue = True
            break
        if not hasFullValue: # char 이 q 인데 기존 dictionary 의 value 중 울음이 가득찬 경우가 없는데 q 가 시작하는 경우 새로운 오리를 추가한다.
          ducks[len(ducks)] = 1
      else: # 울음이 이미 시작한 경우
        if duck.index(char) not in ducks.values(): # 기존 울고있는 오리들중 char 이 이어서 나올 울음이 존재하지 않는 경우
          return - 1
        for idx, val in enumerate(ducks.values()): # 기존 울고있는 오리들중 char 이 이어서 나올 울음이 존재하는 경우 다음 올 울음을 위해 value 에 1을 더한다.
          if duck.index(char) == val:
            ducks[idx] += 1
            break
    # 오리 울음중 quack 의 쌍이 형성되지 않아 남은 경우는 불완전한 울음이니 -1 을 반환한다.
    for val in ducks.values(): 
      if val != 5:
        return -1
    return len(ducks)
      
result = count(str, duck, ducks)

print(result)