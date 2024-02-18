import sys
input = sys.stdin.readline

n = int(input())
towns = []

total = 0
for _ in range(n):
    city, citizen = map(int, input().split())
    total += citizen
    towns.append([city, citizen])

towns.sort()

count = 0
for town in towns:
    city, citizen = town
    count += citizen
    if total / 2 <= count:
        print(city)
        break
