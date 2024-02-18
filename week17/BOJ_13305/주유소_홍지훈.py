import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N: 도시의 개수
roads = list(map(int, input().rstrip().split())) # roads : 인접한 두 도시를 연결하는 도로의 길이. 제일 왼쪽 도로부터 N - 1 개의 자연수
prices = list(map(int, input().rstrip().split())) # prices : 주유소의 리터당 가격

min_price = prices[0]
total_price = min_price * roads[0]

for i in range(1, N - 1):
  if min_price > prices[i]: min_price = prices[i]
  total_price += min_price * roads[i]

print(total_price)
