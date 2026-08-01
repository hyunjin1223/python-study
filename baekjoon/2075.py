# problem: 2075
# tier: silver
import sys
import heapq

# N번째 큰 수 문제

# 빠른 입력
input = sys.stdin.readline

n = int(input())

# 가장 큰 N개의 수만 저장할 최소 힙
heap = []

for _ in range(n):
    numbers = list(map(int, input().split()))

    for num in numbers:
        # 힙 크기가 N보다 작으면 추가
        if len(heap) < n:
            heapq.heappush(heap, num)

        # 현재 수가 힙의 최솟값보다 크면 교체
        elif heap[0] < num:
            heapq.heappushpop(heap, num)

# 힙의 최솟값이 전체에서 N번째로 큰 수
print(heap[0])