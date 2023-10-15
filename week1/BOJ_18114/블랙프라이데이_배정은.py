import sys

def is_combination(C, weights):
    if weights.get(C) is not None: return 1 # 1개의 물건의 무게 합이 충족할 때

    weights_keys = list(weights.keys())
    for key in weights_keys: # 2개의 물건의 무게 합이 충족할 때
        another_key = C - key
        if weights.get(another_key) is not None and (another_key) != key: return 1

    for i in range(len(weights_keys) - 2): # 3개의 물건의 무게 합이 충족할 때
        for j in range(i + 1, len(weights_keys) - 1):
            another_key = C - weights_keys[i] - weights_keys[j]
            if weights.get(another_key) is not None and another_key not in [weights_keys[i], weights_keys[j]]: return 1

    return 0

N, C = map(int, sys.stdin.readline().split()) # N, C
weights = {x : x for x in sorted(list(map(int, sys.stdin.readline().split()))) if x <= C}
print(is_combination(C, weights))