# problem: 1912
# tier: silver
import sys

# 연속합 문제

# 빠른 입력
input = sys.stdin.readline

# 수열 길이
n = int(input())
data = list(map(int, input().split()))

# dp[i] : i번째 수에서 끝나는 최대 연속합
dp = [0] * n
dp[0] = data[0]

# 이전 연속합에 이어 붙일지 새로 시작할지 선택
for i in range(1, n):
    dp[i] = max(data[i], dp[i - 1] + data[i])

# 가장 큰 연속합 출력
print(max(dp))