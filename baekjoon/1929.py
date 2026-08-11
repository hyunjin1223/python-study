# problem: 1929
# tier: silver
import sys

# M 이상 N 이하의 소수 출력
m, n = map(int, sys.stdin.readline().split())

# 처음에는 모두 소수라고 가정
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체로 소수가 아닌 수 제거
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        # i의 배수는 소수가 아니므로 제외
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# M부터 N까지 소수 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)