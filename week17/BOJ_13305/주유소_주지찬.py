import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split(' ')))
gasStations = list(map(int, sys.stdin.readline().split(' ')))

# 첫 번째 도시에서는 무조건 주유
result = road[0] * gasStations[0]
minPrice = gasStations[0]

# 마지막 도시는 이미 도착한 상태이므로 제외
for i in range(1, len(gasStations) - 1):
# 현재 도시의 기름 가격이 이전 도시의 기름 가격보다 싸면
  if gasStations[i] < minPrice:
# 현재 도시의 기름 가격으로 갱신
    minPrice = gasStations[i]
# 최소 기름 가격으로 현재 도시까지 주유
  result += minPrice * road[i]

print(result)
