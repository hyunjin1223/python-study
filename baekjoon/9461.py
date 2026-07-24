# problem: 9461
# tier: silver
import sys

# 빠른 입력
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

# 파도반 수열 저장
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

# 점화식으로 미리 계산
for i in range(6, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

# 결과 출력
for _ in range(t):
    n = int(input())
    print(dp[n])