# problem: 9012
# tier: silver
import sys

# 테스트 케이스 개수 T 입력
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    vps_str = input().strip()
    stack = []
    is_vps = True
    
    for char in vps_str:
        if char == '(':
            # 열린 괄호는 스택에 추가
            stack.append(char)
        else:
            # 닫힌 괄호일 때
            if not stack:
                # 스택이 비어있으면 짝을 맞출 열린 괄호가 없으므로 실패
                is_vps = False
                break
            else:
                # 스택에 열린 괄호가 있다면 하나 제거
                stack.pop()
    
    # 모든 과정을 끝낸 후 스택이 비어있어야 완벽한 짝(VPS)이 됨
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")