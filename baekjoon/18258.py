# problem: 18258
# tier: silver
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    command = input().split()

    # push: 큐의 뒤에 값 추가
    if command[0] == 'push':
        queue.append(command[1])

    # pop: 큐의 앞에서 값 제거
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)

    # size: 큐의 크기 출력
    elif command[0] == 'size':
        print(len(queue))

    # empty: 비어 있으면 1, 아니면 0
    elif command[0] == 'empty':
        print(1 if not queue else 0)

    # front: 큐의 가장 앞 값 확인
    elif command[0] == 'front':
        print(queue[0] if queue else -1)

    # back: 큐의 가장 뒤 값 확인
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)