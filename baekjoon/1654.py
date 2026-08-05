# problem: 1654
# tier: silver
import sys

# 랜선 자르기 문제

# 빠른 입력
input = sys.stdin.readline

# 가지고 있는 랜선 수, 필요한 랜선 수
k, n = map(int, input().split())

# 랜선 길이 입력
lan = [int(input()) for _ in range(k)]

# 가능한 길이 범위
start = 1
end = max(lan)

result = 0

while start <= end:
    # 현재 시도할 랜선 길이
    mid = (start + end) // 2

    # mid 길이로 잘랐을 때 나오는 랜선 개수
    count = 0
    for x in lan:
        count += x // mid

    # 랜선 개수가 충분하면 더 긴 길이 탐색
    if count >= n:
        result = mid
        start = mid + 1

    # 부족하면 길이를 줄임
    else:
        end = mid - 1

# 만들 수 있는 최대 랜선 길이 출력
print(result)