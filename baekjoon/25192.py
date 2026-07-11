# problem: 25192
# tier: silver
import sys

# 채팅방 전체 기록 수 N 입력
input = sys.stdin.readline
n = int(input())

# 곰곰티콘 사용 횟수 카운트
count = 0

# ENTER 이후 채팅한 유저를 저장하는 집합(중복 제거)
users = set()

for _ in range(n):
    log = input().strip()
    
    if log == "ENTER":
        # 새로운 사람이 들어오면 이전까지의 유저 목록을 초기화
        users.clear()
    else:
        # 일반 유저의 채팅 기록인 경우
        if log not in users:
            # 해당 유저가 ENTER 이후 처음 채팅을 치는 것이라면 카운트 증가
            count += 1
            users.add(log)

print(count)