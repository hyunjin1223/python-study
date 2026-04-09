# problem: 9086
# tier: bronze

# 테스트 케이스 개수 입력
T = int(input())

# 문자열 처리 반복
for _ in range(T):
    # 문자열 입력
    s = input()
    # 첫 글자와 마지막 글자 결합 출력
    print(s[0] + s[-1])