# problem: 2501
# tier: bronze

N, K = map(int, input().split())
divisors = []

# 1부터 N까지 나누어 떨어지는 수(약수) 찾기
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)

# K번째 약수가 존재하는지 확인
if len(divisors) < K:
    print(0)
else:
    print(divisors[K-1])