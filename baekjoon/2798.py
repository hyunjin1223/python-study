# problem: 2798
# tier: bronze
from itertools import combinations

# 카드 개수 N, 목표 숫자 M 입력
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

# nCr: N개의 카드 중 3개를 뽑는 모든 조합 확인
for combo in combinations(cards, 3):
    current_sum = sum(combo)
    
    # 합이 M을 넘지 않으면서, 현재까지의 최댓값보다 크면 갱신
    if current_sum <= M:
        max_sum = max(max_sum, current_sum)

print(max_sum)