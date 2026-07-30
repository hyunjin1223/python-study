# problem: 2164
# tier: silver
import sys
from collections import deque

# 카드 2 문제

# 카드 개수
n = int(sys.stdin.readline())

# 1번부터 N번 카드 저장
queue = deque(range(1, n + 1))

# 카드가 한 장 남을 때까지 반복
while len(queue) > 1:
    # 맨 위 카드 버리기
    queue.popleft()

    # 다음 카드를 맨 아래로 이동
    queue.append(queue.popleft())

# 마지막 남은 카드 출력
print(queue[0])