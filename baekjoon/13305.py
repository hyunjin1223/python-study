# problem: 13305
# tier: silver
import sys

# 주유소 문제

# 빠른 입력
input = sys.stdin.readline

# 도시 수
n = int(input())

# 도시 사이 거리와 주유 가격
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 총 비용
total_cost = 0

# 현재까지 가장 싼 기름값
min_price = costs[0]

for i in range(n - 1):
    # 더 싼 주유소면 가격 갱신
    if costs[i] < min_price:
        min_price = costs[i]

    # 현재 최저가로 다음 도시까지 이동
    total_cost += min_price * roads[i]

# 결과 출력
print(total_cost)