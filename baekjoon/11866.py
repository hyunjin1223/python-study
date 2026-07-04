# problem: 11866
# tier: silver
import sys
from collections import deque

# N명의 사람이 원을 이루고 있고, K번째 사람을 계속해서 제거
# 요세푸스 순열(Josephus permutation) 문제
input = sys.stdin.readline
n, k = map(int, input().split())

# 1부터 N까지의 사람을 큐에 삽입
queue = deque(range(1, n + 1))
result = []

while queue:
    # K-1번째 사람까지는 뒤로 보내고 (회전)
    for _ in range(k - 1):
        queue.append(queue.popleft())
    
    # K번째 사람을 제거하여 결과 리스트에 추가
    result.append(str(queue.popleft()))

# 문제 요구 형식에 맞춰 <1, 2, 3> 형태로 출력
print("<" + ", ".join(result) + ">")