# problem: 2908
# tier: bronze

# 두 수 A, B 입력
A, B = input().split()

# 문자열 슬라이싱 [::-1]을 이용해 뒤집은 후 정수로 변환
rev_A = int(A[::-1])
rev_B = int(B[::-1])

# 두 수 중 큰 값을 출력
print(max(rev_A, rev_B))