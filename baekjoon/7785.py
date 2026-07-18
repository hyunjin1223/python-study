# problem: 7785
# tier: silver
import sys

# 빠른 입력 사용
input = sys.stdin.readline

n = int(input())

# 현재 회사에 있는 사람을 저장
office = set()

for _ in range(n):
    name, action = input().split()

    if action == "enter":
        # 출근한 사람 추가
        office.add(name)
    else:
        # 퇴근한 사람 제거
        office.discard(name)

# 이름을 사전순 역순으로 정렬
result = sorted(office, reverse=True)

# 한 줄씩 출력
for name in result:
    sys.stdout.write(name + '\n')