# problem: 17103
# tier: silver
import sys

input = sys.stdin.readline

# 최대 범위까지 소수를 미리 판별
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체로 소수가 아닌 수 제거
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    count = 0

    # 중복을 피하기 위해 n // 2까지만 확인
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1

    print(count)