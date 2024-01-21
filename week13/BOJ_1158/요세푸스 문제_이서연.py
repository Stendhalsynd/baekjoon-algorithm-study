import sys

input = sys.stdin.readline

n, k = map(int, input().split())

people = []

for i in range(1, n + 1):
    people.append(i)

idx = k - 1

print("<", end="")

while people:
    if idx > (len(people) - 1):
        idx %= len(people)
    
    if len(people) == 1:
        print(people.pop(idx), end=">")
    else:
        print(people.pop(idx), end=", ")
        
    idx += (k - 1)