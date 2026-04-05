# problem: 10813
# tier: bronze

# N개 바구니, M번 교환 입력
N, M = map(int, input().split())

# 1~N번 공 초기화
arr = [i + 1 for i in range(N)]

# M번 공 교환 수행
for _ in range(M):
    # 교환할 인덱스 입력
    i, j = map(int, input().split())
    # 값 서로 맞바꿈
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

# 결과 출력
print(*arr)