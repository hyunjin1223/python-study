# problem: 26069
# tier: silver
import sys

# 사람들이 만난 기록의 수 N 입력
input = sys.stdin.readline
n = int(input())

# 무지개 댄스를 추고 있는 사람들을 저장할 집합(Set)
# 처음에는 'ChongChong' 한 명만 춤을 추고 있음
dancing_users = {"ChongChong"}

for _ in range(n):
    a, b = input().split()
    
    # 두 사람 중 한 명이라도 춤을 추고 있다면, 나머지 한 명도 춤을 추게 됨
    if a in dancing_users or b in dancing_users:
        dancing_users.add(a)
        dancing_users.add(b)

# 최종적으로 무지개 댄스를 추는 사람의 수 출력
print(len(dancing_users))