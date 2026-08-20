# problem: 11286
# tier: silver
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        # 절댓값을 첫 번째 기준으로 저장
        # 절댓값이 같으면 실제 값을 기준으로 정렬됨
        heapq.heappush(heap, (abs(x), x))
    else:
        # 힙이 비어 있으면 0 출력
        if not heap:
            print(0)
        else:
            # 우선순위가 가장 높은 값의 실제 값을 출력
            print(heapq.heappop(heap)[1])