# problem: 11047
# tier: silver
import sys

# 동전 0: 준규가 가지고 있는 동전 N종류를 활용해 합을 K로 만드는 최소 동전 개수 구하기.
# 이 문제의 핵심은 "동전의 가치가 서로 배수 관계"에 있다는 점임.
# 따라서 '가장 가치가 큰 동전부터' 최대한 많이 사용하는 그리디(Greedy) 알고리즘이 성립함.

input = sys.stdin.readline
n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# 가장 큰 가치의 동전부터 확인하기 위해 리스트를 뒤집음
coins.reverse()

count = 0
for coin in coins:
    if k == 0:
        break
    
    # 1. 현재 동전으로 만들 수 있는 최대 개수를 더함
    count += k // coin
    
    # 2. 남은 금액을 갱신
    k %= coin

print(count)