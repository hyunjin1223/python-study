# problem: 10815
# tier: silver
import sys

# 빠른 입력
input = sys.stdin.readline

# 카드 개수
n = int(input())

# 가지고 있는 카드 저장
cards = set(map(int, input().split()))

# 확인할 숫자 개수
m = int(input())
checks = list(map(int, input().split()))

results = []

# 카드 존재 여부 확인
for x in checks:
    if x in cards:
        results.append("1")
    else:
        results.append("0")

# 공백으로 구분하여 출력
print(" ".join(results))