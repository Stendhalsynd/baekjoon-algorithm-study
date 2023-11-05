# 구현
from collections import defaultdict

N = int(input())
infos = []
position = [[0 for _ in range(N)] for _ in range(N)]

favorite = defaultdict(set)

for _ in range(N * N):
  info = [int(x) for x in input().split()]
  infos.append(info)
  favorite[info[0]] = info[1:]

def hasNoFriend(array):
  return len(array) == 0

def hasMultiplePosition(array):
    return len(array) > 1


def countFriends(student, row, col):
  count = 0
  if row > 0 and position[row-1][col] in favorite[student]:
    count +=1
  if col > 0 and position[row][col-1] in favorite[student]:
    count +=1
  if row < N - 1 and position[row+1][col] in favorite[student]:
    count +=1
  if col < N - 1 and position[row][col+1] in favorite[student]:
    count +=1
  return count

def countEmptyPositions(row, col):
  count = 0
  if row > 0 and position[row-1][col] == 0:
    count +=1
  if col > 0 and position[row][col-1] == 0:
    count +=1
  if row < N - 1 and position[row+1][col] == 0:
    count +=1
  if col < N - 1 and position[row][col+1] == 0:
    count +=1
  return count

def maxFriends(student):
  max = -1
  friends = []
  for r in range(N):
    for c in range(N):
      friendsTotal = countFriends(student, r, c)
      if position[r][c] == 0 and friendsTotal >= max:
        if friendsTotal > max:
          friends.clear()
          max = friendsTotal
        friends.append([r + 1, c + 1])

  if hasNoFriend(friends) or hasMultiplePosition(friends):
    return False, friends
  else:
    return True, friends[0]
  
def maxEmpty(friends):
  max = 0
  result = []

  if len(friends) == 0:
    for r in range(len(position)):
      for c in range(len(position[0])):
        emptyPos = countEmptyPositions(r, c)
        if emptyPos >= max:
          if emptyPos > max:
            result.clear()
            max = emptyPos
          result.append([r + 1, c + 1])
  else:
    for r, c in friends:
      emptyPos = countEmptyPositions(r - 1, c - 1)
      if emptyPos >= max:
        if emptyPos > max:
          result.clear()
          max = emptyPos
        result.append([r, c])

  if hasMultiplePosition(result):
    return False, result
  else:
    return True, result[0]
  
def minRowNumber(emptyResult):
  emptyResult.sort(key = lambda x: x[0])
  minRow = emptyResult[0][0]
  filteredResults = list(filter(lambda x: x[0] == minRow, emptyResult))

  if hasMultiplePosition(filteredResults):
    return False, filteredResults
  else:
    return True, filteredResults[0]
  
def minColNumber(minRows):
  minRows.sort(key = lambda x: x[1])
  return minRows[0]

def getPosition(student):
  hasMaxFriends, friends = maxFriends(student)
  if hasMaxFriends: 
    return friends
  else:

    hasmaxEmpty, emptyResult = maxEmpty(friends)
    if hasmaxEmpty: 
      return emptyResult
    else:

      hasMinRowNumber, minRows = minRowNumber(emptyResult)
      if hasMinRowNumber: 
        return minRows
      else: 
        return minColNumber(minRows)

def updatePosition():
  for student in favorite:
    pos = getPosition(student)
    row, col = pos[0] - 1, pos[1] - 1
    position[row][col] = student

def totalSatisfaction():
  sum = 0
  for r in range(N):
    for c in range(N):
      sum += calcSatisfaction(countFriends(position[r][c], r, c))
  return sum

def calcSatisfaction(total):
  if total == 0:
    return 0
  elif total == 1:
    return 1
  elif total == 2:
    return 10
  elif total == 3:
    return 100
  elif total == 4:
    return 1000

updatePosition()
print(totalSatisfaction())
