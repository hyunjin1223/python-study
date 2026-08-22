# problem: 11399
# tier: silver
import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

# 인출 시간이 짧은 사람부터 처리해야 전체 대기 시간이 최소가 됨
p.sort()

total_time = 0
current_sum = 0

for time in p:
    # 현재 사람까지 걸리는 시간을 누적
    current_sum += time

    # 각 사람이 기다린 시간을 모두 더함
    total_time += current_sum

print(total_time)