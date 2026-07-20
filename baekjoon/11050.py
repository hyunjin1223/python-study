# problem: 11050
# tier: bronze
import sys

# N, K 입력
n, k = map(int, sys.stdin.readline().split())

# 팩토리얼 계산
def factorial(num):
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res

# 이항 계수 계산
result = factorial(n) // (factorial(k) * factorial(n - k))

# 결과 출력
print(result)