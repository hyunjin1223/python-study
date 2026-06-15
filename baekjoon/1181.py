# problem: 1181
# tier: silver
import sys

# 데이터 개수가 많을 수 있으므로 빠른 입력 사용
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

# 1. set()으로 변환하여 중복된 단어 제거 후 다시 리스트로 변환
words = list(set(words))

# 2. 정렬 조건 설정
# 1순위: 단어의 길이 (len(x))
# 2순위: 알파벳 사전 순 (x)
words.sort(key=lambda x: (len(x), x))

# 정렬된 단어들을 한 줄씩 출력
for word in words:
    print(word)