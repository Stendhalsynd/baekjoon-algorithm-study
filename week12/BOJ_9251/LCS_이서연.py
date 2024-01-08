import sys

input = sys.stdin.readline

str1 = input()
str2 = input()

if str1[-1].isalpha() == False:
    str1 = str1[:-1]

if str2[-1].isalpha() == False:
    str2 = str2[:-1]


d = [0] * len(str2)

for i in range(len(str1)):
    value = 0
    
    for j in range(len(str2)):
        if value < d[j]:
            value = d[j]        
        elif str1[i] == str2[j]:
            d[j] = value + 1

print(max(d))