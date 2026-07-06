# problem: 28278
# tier: silver
import sys

# 명령의 수 N이 최대 1,000,000개이므로 sys.stdin.readline 필수
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    
    # 1 X: 정수 X를 스택에 넣는다.
    if command[0] == '1':
        stack.append(command[1])
    
    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력, 없다면 -1 출력
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print("-1")
            
    # 3: 스택에 들어있는 정수의 개수 출력
    elif command[0] == '3':
        print(len(stack))
        
    # 4: 스택이 비어있으면 1, 아니면 0 출력
    elif command[0] == '4':
        print(1 if not stack else 0)
        
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력, 없다면 -1 출력
    elif command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print("-1")