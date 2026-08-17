# problem: 2559
# tier: silver
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

# 처음 K일의 온도 합을 구해 초기값으로 사용
current_sum = sum(temps[:k])
max_sum = current_sum

# 한 칸씩 이동하면서 구간의 합을 갱신
for i in range(k, n):
    # 새로운 값을 더하고 이전 구간의 첫 값을 제거
    current_sum += temps[i]
    current_sum -= temps[i - k]

    # 지금까지의 구간 합 중 최댓값 저장
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)