# problem: 1330
# tier: bronze

# 두 정수 입력 및 변환
A, B = map(int, input().split())

# 크기 비교 후 결과 출력
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")