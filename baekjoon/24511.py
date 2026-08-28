# problem: 24511
# tier: silver
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 0은 큐, 1은 스택
types = list(map(int, input().split()))

# 각 자료구조에 들어 있는 초기 값
initial_values = list(map(int, input().split()))

m = int(input())
new_elements = list(map(int, input().split()))

# 스택은 값을 넣어도 다시 같은 값이 나오므로 제외
# 실제로 값이 바뀌는 큐만 deque에 저장
dq = deque()

for i in range(n):
    if types[i] == 0:
        dq.append(initial_values[i])

results = []

for x in new_elements:
    # 새로운 값이 들어오면 가장 뒤의 값이 나옴
    dq.appendleft(x)
    results.append(str(dq.pop()))

print(" ".join(results))