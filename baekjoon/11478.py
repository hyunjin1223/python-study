# problem: 11478
# tier: silver

import sys

# 문자열 입력
s = input().strip()

# 부분 문자열 저장
substrings = set()

# 모든 부분 문자열 생성
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.add(s[i:j])

# 서로 다른 부분 문자열 개수 출력
print(len(substrings))