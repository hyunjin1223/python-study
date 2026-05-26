# problem: 2720
# tier: bronze

T = int(input())

# 동전 단위: 25c, 10c, 5c, 1c
coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    res = []
    for coin in coins:
        res.append(C // coin)
        C %= coin
    print(*res)