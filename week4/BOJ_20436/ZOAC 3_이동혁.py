left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']

left_start, right_start = map(str, input().split())
vocab = list(map(str, input()))

keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

def find_index(string):
    i = 0
    for row in keyboard:
        j = 0
        for element in row:
            if string == keyboard[i][j]:
                return i, j
            j += 1
        i += 1

left_loc, right_loc = [-1, -1], [-1, -1]
left_loc[0], left_loc[1] = find_index(left_start)
right_loc[0], right_loc[1] = find_index(right_start)

total_distance = 0

for element in vocab:
    if element in left:
        loc_x, loc_y = find_index(element)
        total_distance += abs(left_loc[0] - loc_x) + abs(left_loc[1] - loc_y)
        left_loc[0] = loc_x
        left_loc[1] = loc_y
        total_distance += 1
    else:
        loc_x, loc_y = find_index(element)
        total_distance += abs(right_loc[0] - loc_x) + abs(right_loc[1] - loc_y)
        right_loc[0] = loc_x
        right_loc[1] = loc_y
        total_distance += 1

print(total_distance)