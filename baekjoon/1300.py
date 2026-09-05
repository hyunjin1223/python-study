# problem: 1300
# tier: gold
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k
result = 0

while start <= end:
    mid = (start + end) // 2

    # mid 이하인 수의 개수
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)

    # k개 이상이면 더 작은 값 탐색
    if count >= k:
        result = mid
        end = mid - 1

    # k개보다 적으면 더 큰 값 탐색
    else:
        start = mid + 1

print(result)