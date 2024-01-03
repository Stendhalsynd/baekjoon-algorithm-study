import sys
input = sys.stdin.readline
from collections import Counter

'''
같은 구성
1. 두 단어가 같은 종류의 문자로 구성
2. 같은 문자는 같은 개수만큼 존재

비슷한 단어
1. 같은 구성
2. 한 단어서 한 문자를 더하거나 / 빼거나 / 다른 문자로 치환시 같은 구성
'''
N = int(input()) # N: 단어의 개수
compare = input().rstrip() # compare: 비교할 첫 단어
count_compare = Counter(compare)

count = 0 # count: 비슷한 단어의 수

def counter(compare):
  compare_info = {} # info: 각 문자가 몇번 등장했는지 
  for char in compare:
    if char in compare_info:
      compare_info[char] += 1
    else:
      compare_info[char] = 1
  return compare_info

info = counter(compare)

def is_same_compose(word: str) -> bool:
  word_info = counter(word)
  if sorted(word_info.keys()) != sorted(info.keys()):
    return False
  for key in info.keys():
    if info[key] != word_info[key]:
      return False
  return True

for _ in range(N - 1):
  word_info = {}
  word = input().rstrip()
  count_word = Counter(word)

  # 1. word 의 글자수가 compare 보다 1 작을때 (문자 더하기)
  if len(compare) - len(word) == 1:
    add_char = [char for char in count_word.keys() if count_compare[char] - count_word[char] == 1]

    more_compare = False
    is_valid = True

    for char in count_word.keys():
      if count_compare[char] - count_word[char] == 1:
        more_compare = True
      elif count_word[char] - count_compare[char] > 0:
        is_valid = False
    if more_compare and is_valid: # 1. word 의 모든 문자를 compare 가 갖고 있으나 한 문자에 대해서 한개 더 갖고 있는 경우
      count += 1
    elif all(count_compare[char] == count_word[char] for char in count_word.keys()): # 2. word의 모든 문자를 같은 수만큼 compare가 갖고 다른 종류의 문자를 하나 더 가질 경우
      count += 1

  # 2. word 의 글자수와 compare 가 같을때 (같은 구성 / 문자 교체)
  elif len(compare) == len(word):
    if is_same_compose(word): 
      count += 1 # 같은 구성
    else: # 문자 교체
      is_valid_one = True
      for char in count_word.keys():
        if count_word[char] - count_compare[char] > 1:
          is_valid_one = False
          break
      diff_char = [char for char in count_word.keys() if count_word[char] != count_compare[char]]
      if len(diff_char) == 1 and is_valid_one: # 1. AAAB, AAAC 같은 경우
        count += 1
      
      more_compare = False
      more_word = False
      is_valid_two = True

      for char in count_word.keys():
        if count_word[char] - count_compare[char] == 1:
          if more_word == False:
            more_word = True
          else:
            is_valid_two = False
            break
        elif count_compare[char] - count_word[char] == 1:
          if more_compare == False:
            more_compare = True
          else:
            is_valid_two = False
            break
      if more_compare and more_word and is_valid_two: # AAAB, ABBA 같은 경우
        count += 1

  # 3. word 의 글자수가 compare 보다 1 클때 (문자 빼기)
  if len(word) - len(compare) == 1:
    minus_char = [char for char in count_word.keys() if count_word[char] - count_compare[char] == 1]
    if len(minus_char) == 1: # AAAB, AAAAB 같은 경우
      count += 1
    elif all(count_word[char] == count_compare[char] for char in count_compare.keys()): # AAAB, AAABC 같은 경우
      count += 1

print(count)