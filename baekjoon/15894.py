# problem: 15894
# tier: bronze

# 가장 아랫부분의 정사각형 개수 n 입력
n = int(input())

# 실루엣의 둘레는 항상 한 변의 길이 n인 정사각형의 둘레와 같음
# 윗변 합 = n, 밑변 합 = n, 좌우 높이 합 = 2n
print(4 * n)