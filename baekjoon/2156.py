# problem: 2156
# tier: silver
import sys

# 포도주 시식 문제

# 빠른 입력
input = sys.stdin.readline

# 포도주 잔 개수
n = int(input())

# 포도주 양 저장 (1번부터 사용)
wine = [0] * 10001
for i in range(1, n + 1):
    wine[i] = int(input())

# dp[i] : i번째 잔까지 고려했을 때 마실 수 있는 최대 양
dp = [0] * 10001

# 초기값
dp[1] = wine[1]

if n >= 2:
    dp[2] = wine[1] + wine[2]

# 세 잔 연속으로 마실 수 없도록 경우의 수 비교
for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],                         # 현재 잔을 마시지 않음
        dp[i - 2] + wine[i],               # 현재 잔만 마심
        dp[i - 3] + wine[i - 1] + wine[i]  # 현재 잔과 이전 잔을 마심
    )

# 최대 포도주 양 출력
print(dp[n])