# problem: 12789
# tier: silver
import sys

# 학생 수 입력
input = sys.stdin.readline
n = int(input())

# 학생 순서
students = list(map(int, input().split()))

# 옆 대기 공간(스택)
stack = []
# 다음 차례
current = 1

for student in students:
    # 스택으로 이동
    stack.append(student)

    # 순서가 맞으면 간식 받기
    while stack and stack[-1] == current:
        stack.pop()
        current += 1

# 모두 받았으면 Nice
if not stack:
    print("Nice")
else:
    print("Sad")