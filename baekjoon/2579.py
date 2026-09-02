# problem: 2579
# tier: silver
import sys

input = sys.stdin.readline

n = int(input())
stairs = [0] * 301

for i in range(1, n + 1):
    stairs[i] = int(input())

dp = [0] * 301

# 첫 번째 계단
dp[1] = stairs[1]

if n >= 2:
    dp[2] = stairs[1] + stairs[2]

if n >= 3:
    # 3번째 계단은 1->3 또는 2->3
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    # i-2에서 두 칸 올라오기
    case1 = dp[i - 2] + stairs[i]

    # i-3 -> i-1 -> i
    case2 = dp[i - 3] + stairs[i - 1] + stairs[i]

    dp[i] = max(case1, case2)

print(dp[n])