# problem: 1931
# tier: silver
import sys

# 회의실 배정 문제

# 빠른 입력
input = sys.stdin.readline

# 회의 개수
n = int(input())

# 시작 시간과 종료 시간 저장
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

# 종료 시간이 빠른 순서로 정렬
# 종료 시간이 같으면 시작 시간이 빠른 순서로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    # 이전 회의가 끝난 후 시작할 수 있으면 선택
    if start >= last_end_time:
        count += 1
        last_end_time = end

# 선택한 회의 개수 출력
print(count)