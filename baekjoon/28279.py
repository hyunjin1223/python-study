# problem: 28279
# tier: silver
import sys
from collections import deque

# 명령의 수가 최대 1,000,000개이므로 sys.stdin.readline 사용
# 양방향 삽입/삭제가 빈번하므로 collections.deque가 가장 효율적임
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    cmd_type = command[0]
    
    # 1 X: 정수 X를 덱의 앞에 넣는다.
    if cmd_type == '1':
        dq.appendleft(command[1])
    
    # 2 X: 정수 X를 덱의 뒤에 넣는다.
    elif cmd_type == '2':
        dq.append(command[1])
        
    # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력, 없다면 -1
    elif cmd_type == '3':
        print(dq.popleft() if dq else -1)
        
    # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력, 없다면 -1
    elif cmd_type == '4':
        print(dq.pop() if dq else -1)
        
    # 5: 덱에 들어있는 정수의 개수 출력
    elif cmd_type == '5':
        print(len(dq))
        
    # 6: 덱이 비어있으면 1, 아니면 0 출력
    elif cmd_type == '6':
        print(1 if not dq else 0)
        
    # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력, 없다면 -1
    elif cmd_type == '7':
        print(dq[0] if dq else -1)
        
    # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력, 없다면 -1
    elif cmd_type == '8':
        print(dq[-1] if dq else -1)