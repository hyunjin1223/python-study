# problem: 1037
# tier: bronze
import sys

# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수여야 하고, A가 1과 N이 아니어야 함.
# 어떤 수 N의 진짜 약수들이 모두 주어졌을 때, N을 구하는 문제.

# 1. 진짜 약수의 개수 입력
count = int(sys.stdin.readline())

# 2. 진짜 약수 리스트 입력
divisors = list(map(int, sys.stdin.readline().split()))

# N의 진짜 약수들 중 가장 작은 값과 가장 큰 값을 곱하면 N이 됨.
# 예: N=12의 진짜 약수 [2, 3, 4, 6] -> 2 * 6 = 12
# 약수가 하나뿐인 경우(예: N=4, 약수 [2])는 그 수를 제곱하면 됨.
# min * max 로직은 약수가 하나일 때도 (2 * 2) 동일하게 적용됨.

print(min(divisors) * max(divisors))