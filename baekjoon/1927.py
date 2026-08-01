# problem: 1927
# tier: silver
import sys
import heapq

# 최소 힙 문제

# 빠른 입력
input = sys.stdin.readline

n = int(input())

# 최소 힙 저장
heap = []

for _ in range(n):
    x = int(input())

    # 자연수이면 힙에 추가
    if x > 0:
        heapq.heappush(heap, x)

    # 0이면 최솟값 출력
    else:
        # 힙이 비어 있으면 0 출력
        if not heap:
            print(0)

        # 가장 작은 값 제거 후 출력
        else:
            print(heapq.heappop(heap))