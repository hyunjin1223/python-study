# problem: 11279
# tier: silver
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        # heapq는 최소 힙이므로 음수로 바꿔 저장
        heapq.heappush(heap, -x)
    else:
        # 힙이 비어 있으면 0 출력
        if not heap:
            print(0)
        else:
            # 꺼낸 음수를 다시 양수로 바꿔 출력
            print(-heapq.heappop(heap))