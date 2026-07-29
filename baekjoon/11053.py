# problem: 11053
# tier: silver
import sys

# 가장 긴 증가하는 부분 수열(LIS)

# 빠른 입력
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp[i] = i번째 원소를 마지막으로 하는 LIS 길이
dp = [1] * n

# 이전 원소들과 비교하면서 LIS 길이 갱신
for i in range(n):
    for j in range(i):
        # 증가하는 경우
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 LIS 길이 출력
print(max(dp))