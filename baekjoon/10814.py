# problem: 10814
# tier: silver

import sys

# 빠른 입력
input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    # 나이, 이름 입력
    age, name = input().split()
    members.append((int(age), name))

# 나이순 정렬 (같은 나이는 입력 순서 유지)
members.sort(key=lambda x: x[0])

# 결과 출력
for age, name in members:
    print(age, name)