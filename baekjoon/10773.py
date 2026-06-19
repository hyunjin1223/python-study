# problem: 10773
# tier: silver
import sys

# 정수 K가 최대 100,000개이므로 빠른 입력 사용
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    num = int(input())
    
    if num == 0:
        # 정수가 0일 경우 가장 최근에 쓴 수를 지움 (스택 pop)
        # 문제 조건상 0일 때 지울 수 있는 수가 있음을 보장함
        stack.pop()
    else:
        # 0이 아닐 경우 해당 수를 스택에 추가
        stack.append(num)

# 최종적으로 스택에 남아있는 수들의 합을 출력
# 비어있을 경우 sum()은 0을 반환함
print(sum(stack))