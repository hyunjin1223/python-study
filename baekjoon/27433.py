# problem: 27433
# tier: bronze
import sys

# 정수 N 입력 (0 <= N <= 20)
# 10872번과 동일한 팩토리얼 문제이지만 입력 범위가 조금 더 넓음 (N=20까지)
n = int(sys.stdin.readline())

# 재귀 함수를 이용한 팩토리얼 구현
def factorial(num):
    # 0! 과 1! 은 1
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(n))

# recursive factorial for small N