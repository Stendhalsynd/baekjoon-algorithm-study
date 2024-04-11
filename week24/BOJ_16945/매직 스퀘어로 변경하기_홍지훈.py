import sys, itertools
input = sys.stdin.readline

arr_A = []
sum_goal = 15
for _ in range(3):
  args = list(map(int, input().rstrip().split()))
  arr_A.append(args)

def generate_magic_squares():
  permutations = itertools.permutations(range(1, 10))

  magic_squares = []
  for perm in permutations:
    if perm[0] + perm[1] + perm[2] == 15 and \
      perm[3] + perm[4] + perm[5] == 15 and \
      perm[6] + perm[7] + perm[8] == 15 and \
      perm[0] + perm[3] + perm[6] == 15 and \
      perm[1] + perm[4] + perm[7] == 15 and \
      perm[2] + perm[5] + perm[8] == 15 and \
      perm[0] + perm[4] + perm[8] == 15 and \
      perm[2] + perm[4] + perm[6] == 15:
      magic_square = [[perm[0], perm[1], perm[2]], 
                      [perm[3], perm[4], perm[5]], 
                      [perm[6], perm[7], perm[8]]]
      magic_squares.append(magic_square)
  
  return magic_squares

magic_squares = generate_magic_squares()

def magic_square_cost(square):
  min_cost = sys.maxsize
  for magic_square in magic_squares:
    cost = sum(abs(square[i][j] - magic_square[i][j]) for i in range(3) for j in range(3))
    min_cost = min(min_cost, cost)
  return min_cost

min_cost = magic_square_cost(arr_A)
print(min_cost)