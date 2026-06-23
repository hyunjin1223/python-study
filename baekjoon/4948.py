# problem: 4948
# tier: silver
import sys

# 베르트랑 공준: n < x <= 2n 범위 내에 소수가 반드시 적어도 하나 존재함
# 입력 범위 n이 최대 123,456이므로, 2n인 246,912까지의 소수를 미리 구해놓는 것이 효율적임

# 1. 에라토스테네스의 체를 사용하여 최대 범위까지 소수 판별 리스트 생성
MAX = 123456 * 2
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

# 입력을 계속 받으며 0이 들어오면 종료
input = sys.stdin.read
queries = map(int, input().split())

for n in queries:
    if n == 0:
        break
    
    # n보다 크고 2n보다 작거나 같은 범위의 소수 개수 카운트
    # 슬라이싱과 sum()을 사용하면 반복문보다 빠르게 계산 가능
    print(sum(is_prime[n + 1 : 2 * n + 1]))