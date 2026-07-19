# problem: 4949
# tier: silver
import sys

# 여러 줄 입력을 한 번에 읽음
input = sys.stdin.read

def solve():
    # 줄 단위로 나누기
    lines = input().splitlines()

    for line in lines:
        # "."만 입력되면 종료
        if line == ".":
            break

        # 괄호를 저장할 스택
        stack = []
        is_balanced = True

        # 문장의 모든 문자 확인
        for char in line:
            # 여는 괄호는 스택에 저장
            if char == '(' or char == '[':
                stack.append(char)

            # ')'가 나오면 '('와 짝 확인
            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_balanced = False
                    break
                stack.pop()

            # ']'가 나오면 '['와 짝 확인
            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_balanced = False
                    break
                stack.pop()

        # 스택이 비어 있어야 모든 괄호의 짝이 맞음
        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

solve()