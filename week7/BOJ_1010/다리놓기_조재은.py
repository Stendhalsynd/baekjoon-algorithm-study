'''
(방법1)
1. 다리를 지을 때 겹칠 수없기 때문에 규칙을 찾아보면 서쪽에는 1개, 동쪽에는 n개가 있을 때 다리는 n개 지을 수 있다.
2. 서쪽의 사이트 개수와 동쪽의 사이트 개수가 똑같다면 다리는 1개 지을 수 있다.
3. 서쪽의 사이트 개수가 n, 동쪽의 사이트 개수가 m이라면 (서쪽에 n개, 동쪽에 m-1 개로 지울 수 있는 다리) + (서쪽에 n-1개, 동쪽에 m-1개로 지을 수 있는 다리) 와 같다.
(방법2)
조합을 이용해서 해결할 수 있다. 서로 다른 m개에서 n개를 고르는 경우의 수를 구해준다.
- factorial을 정의하고 조합을 이용하여 다리의 개수를 구한다.
- m C n = m!/n!*(m-n)!
'''
import math

T = int(input()) # 테스트 케이스 수
result = []

for _ in range(T):
    N, M = map(int, input().split()) # 서, 동 사이트의 개수

    bridge = math.factorial(M) / (math.factorial(N) * math.factorial(M-N)) # 조합 공식
    result.append(int(bridge))

print(result)