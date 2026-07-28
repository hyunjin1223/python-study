# problem: 11659
# tier: silver
import sys

# 구간 합 구하기 4

# 빠른 입력
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 누적 합 배열 생성
# prefix_sum[i] = 1번부터 i번까지의 합
prefix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + data[i]

# 구간 합 계산
for _ in range(m):
    i, j = map(int, input().split())

    # i~j 구간 합
    print(prefix_sum[j] - prefix_sum[i - 1])