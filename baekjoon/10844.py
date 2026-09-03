# problem: 10844
# tier: silver
import sys

input = sys.stdin.readline

n = int(input())
mod = 1000000000

# dp[i][j] = i자리 계단 수 중 마지막 숫자가 j인 경우의 수
dp = [[0] * 10 for _ in range(n + 1)]

# 첫 자리는 0이 될 수 없음
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        # 0은 1에서만 올 수 있음
        if j == 0:
            dp[i][j] = dp[i - 1][1]

        # 9는 8에서만 올 수 있음
        elif j == 9:
            dp[i][j] = dp[i - 1][8]

        # 나머지는 양쪽 숫자에서 올 수 있음
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

        dp[i][j] %= mod

# 마지막 숫자에 상관없이 모두 더함
print(sum(dp[n]) % mod) 