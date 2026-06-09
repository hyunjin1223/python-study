# problem: 2581
# tier: bronze

M = int(input())
N = int(input())

primes = []

for num in range(M, N + 1):
    if num < 2:
        continue
    
    is_prime = True
    # 2부터 해당 수의 제곱근까지 확인하여 소수 판별
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)

# 소수가 존재하는 경우 합계와 최솟값 출력
if primes:
    print(sum(primes))
    print(min(primes))
else:
    # 소수가 없는 경우 -1 출력
    print(-1)