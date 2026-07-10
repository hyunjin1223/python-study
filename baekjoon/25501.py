# problem: 25501
# tier: bronze
import sys

# 재귀 함수를 이용한 팰린드롬 판별 및 호출 횟수 측정
# 팰린드롬이란 앞에서 읽었을 때와 뒤에서 읽었을 때가 똑같은 문자열을 의미함

def recursion(s, l, r, count):
    # 호출될 때마다 카운트 1 증가
    count += 1
    # 1. 왼쪽 인덱스가 오른쪽보다 크거나 같으면 모든 문자를 검사한 것이므로 팰린드롬임 (1 반환)
    if l >= r:
        return 1, count
    # 2. 양 끝 문자가 다르면 팰린드롬이 아님 (0 반환)
    elif s[l] != s[r]:
        return 0, count
    # 3. 양 끝이 같으면 인덱스를 좁혀서 재귀 호출
    else:
        return recursion(s, l + 1, r - 1, count)

def isPalindrome(s):
    # 문자열 s, 시작 인덱스 0, 끝 인덱스 len(s)-1, 초기 카운트 0 전달
    return recursion(s, 0, len(s) - 1, 0)

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    s = input().strip()
    # 팰린드롬 여부와 recursion 함수 호출 횟수를 출력
    result, call_count = isPalindrome(s)
    print(f"{result} {call_count}")