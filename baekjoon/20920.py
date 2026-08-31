# problem: 20920
# tier: silver
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
word_counts = {}

for _ in range(n):
    word = input().strip()

    # 길이가 m 미만인 단어는 제외
    if len(word) < m:
        continue

    # 단어가 나온 횟수를 저장
    word_counts[word] = word_counts.get(word, 0) + 1

# 빈도수 내림차순 → 길이 내림차순 → 사전순으로 정렬
sorted_words = sorted(
    word_counts.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])
)

# 정렬된 단어만 출력
for word, _ in sorted_words:
    print(word)