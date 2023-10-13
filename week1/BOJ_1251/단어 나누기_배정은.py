import sys

word = sys.stdin.readline().rstrip()
min_word = ''

for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        a, b, c = word[:i + 1], word[i + 1:j + 1], word[j + 1:]
        a, b, c = ''.join(list(a)[::-1]), ''.join(list(b)[::-1]), ''.join(list(c)[::-1])

        min_word = a + b + c if min_word == '' or min_word >= a + b + c else min_word # 사전 순으로 가장 앞에 있는 단어 출력

print(min_word)