# problem: 2346
# tier: silver
import sys
from collections import deque

# 풍선의 개수 N 입력
input = sys.stdin.readline
n = int(input())

# 풍선 안의 숫자를 입력받아 (인덱스+1, 종이의 숫자) 형태로 저장
# deque의 rotate를 사용하기 위해 deque로 생성
balloons = deque(enumerate(map(int, input().split()), start=1))

result = []

while balloons:
    # 1. 현재 가장 앞에 있는 풍선을 터뜨림
    idx, paper = balloons.popleft()
    result.append(str(idx))
    
    # 풍선이 더 이상 없으면 이동할 필요 없음
    if not balloons:
        break
    
    # 2. 종이에 적힌 숫자만큼 이동
    # 양수면 오른쪽으로, 음수면 왼쪽으로 이동
    # popleft() 했으므로 양수는 1을 빼서 회전
    if paper > 0:
        balloons.rotate(-(paper - 1))
    else:
        balloons.rotate(-paper)

# 결과 출력
print(" ".join(result))