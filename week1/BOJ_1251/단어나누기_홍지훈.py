import sys

word = sys.stdin.readline().rstrip()

words = []

for i in range(1, len(word) - 1):
  for j in range(i + 1, len(word)):
    word1, word2, word3 = word[:i][::-1], word[i: j][::-1], word[j:][::-1]
    words.append(word1+word2+word3)

words.sort()

print(words[0])