# problem: 1978
# tier: bronze

n = int(input())
numbers = list(map(int, input().split()))
prime_cnt = 0

for num in numbers:
    # 1은 소수가 아님
    if num < 2:
        continue
    
    is_prime = True
    # 2부터 해당 수의 제곱근까지 나누어 떨어지는지 확인
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_cnt += 1

print(prime_cnt)