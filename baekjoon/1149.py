# problem: 1149
# tier: silver
import sys

# RGB 거리 문제

# 빠른 입력
input = sys.stdin.readline

# 집 개수
n = int(input())

# 각 집의 빨강, 초록, 파랑 비용 저장
costs = []

for _ in range(n):
    costs.append(list(map(int, input().split())))

# 이전 집과 다른 색을 선택하면서 최소 비용 갱신
for i in range(1, n):
    # 현재 집을 빨강으로 칠하는 경우
    costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])

    # 현재 집을 초록으로 칠하는 경우
    costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])

    # 현재 집을 파랑으로 칠하는 경우
    costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

# 마지막 집까지 칠했을 때의 최소 비용
print(min(costs[n - 1]))