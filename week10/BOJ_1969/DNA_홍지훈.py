from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N : DNA 의 수, M : 문자열의 길이

min_hamming_sum = 0
min_dna = ''
# Hamming Distance = 길이가 같은 두 DNA 가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수

dna_input = [input().rstrip() for _ in range(N)]

for i in range(M):
  counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  for dna in dna_input:
    counter[dna[i]] += 1
  
  max_val = 0
  max_dna = ''
  for dna, val in counter.items():
    if val > max_val:
      max_val = val
      max_dna = dna
  min_dna = min_dna + max_dna
  min_hamming_sum += N - counter[max_dna]

print(min_dna)
print(min_hamming_sum)

# from itertools import product
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().rstrip().split()) # N : DNA 의 수, M : 문자열의 길이

# min_hamming_sum = M * N
# min_dna = ''
# # Hamming Distance = 길이가 같은 두 DNA 가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수

# def calc_hamming_dist(dna1: str, dna2: str) -> int:
#   count = 0

#   for char1, char2 in zip(dna1, dna2):
#     if char1 != char2:
#       count += 1

#   return count

# dna_info = ['A', 'C', 'G', 'T']
# dna_list = [''.join(dna) for dna in list(product(dna_info, repeat=M))] # 가능한 dna 후보 리스트
# dna_input = []

# for _ in range(N):
#   dna_input.append(input().rstrip())

# for dna in dna_list:
#   hd_sum = 0
#   for input in dna_input:
#     hd_sum += calc_hamming_dist(dna, input)
#   if hd_sum < min_hamming_sum:
#     min_dna = dna
#     min_hamming_sum = hd_sum

# print(min_dna)
# print(min_hamming_sum)